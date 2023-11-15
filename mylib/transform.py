from pyspark.sql import SparkSession

# from pyspark.sql.functions import col


def load(dataset="dbfs:/FileStore/databricks_project/top50MusicFrom2010-2019.csv"):
    spark = SparkSession.builder.appName("Read CSV").getOrCreate()

    # Load CSV and transform it by inferring schema
    top50MusicFrom2010_2019_df = spark.read.csv(dataset, header=True, inferSchema=True)

    # Rename columns to remove invalid characters
    new_column_names = [
        col.replace(" ", "_").replace(",", "").replace(";", "")
        for col in top50MusicFrom2010_2019_df.columns
    ]
    top50MusicFrom2010_2019_df = top50MusicFrom2010_2019_df.toDF(*new_column_names)

    # Transform into a Delta Lakes table and store it
    top50MusicFrom2010_2019_df.write.format("delta").mode("overwrite").saveAsTable(
        "top50MusicFrom2010_2019_delta"
    )

    # Check Delta table protocol version
    history_df = spark.sql("DESCRIBE HISTORY top50MusicFrom2010_2019_delta")

    # Find the protocol version in the operationParameters column
    protocol_version_row = (
        history_df.filter("operation = 'WRITE'").select("operationParameters").first()
    )

    if protocol_version_row:
        protocol_version_str = protocol_version_row[0]
        protocol_version = [
            param.split("=")
            for param in protocol_version_str.split(", ")
            if "delta.protocol" in param
        ]

        if protocol_version:
            protocol_version = protocol_version[0][1]
            print("Current Delta Table Protocol Version:", protocol_version)

            # Upgrade Delta table protocol version if necessary
            if protocol_version != "2.5":
                spark.sql(
                    "ALTER TABLE top50MusicFrom2010_2019_delta SET TBLPROPERTIES \
                        ('delta.columnMapping.mode' = 'name', \
                            'delta.minReaderVersion' = '2', \
                            'delta.minWriterVersion' = '5')"
                )

    num_rows = top50MusicFrom2010_2019_df.count()
    print(num_rows)

    return "finished transform and load"


if __name__ == "__main__":
    load()
