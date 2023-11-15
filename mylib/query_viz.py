from pyspark.sql import SparkSession
import matplotlib.pyplot as plt


def query_transform():
    """
    Run a predefined SQL query on a Spark DataFrame.

    Returns:
        DataFrame: Result of the SQL query.
    """
    # Create a Spark session
    spark = SparkSession.builder.appName("Query").getOrCreate()

    # Define the SQL query
    query = "SELECT * FROM top50musicfrom2010_2019_delta " 'WHERE artist = "Rihanna"'

    # Run the SQL query
    query_result = spark.sql(query)

    return query_result


# Run the query
result_df = query_transform()

# Show the result (you can also perform further
# actions like saving the result or displaying statistics)
result_df.show()


def simple_plot(df):
    """
    Create a simple plot based on the DataFrame.

    Parameters:
        df (DataFrame): Input DataFrame.

    Returns:
        None
    """
    # Create a histogram
    plt.figure(figsize=(12, 6))
    plt.hist(
        df.select("year").toPandas()["year"],
        bins=range(
            df.select("year").toPandas()["year"].min(),
            df.select("year").toPandas()["year"].max() + 1,
        ),
        color="green",
        alpha=0.7,
        edgecolor="black",
    )
    plt.xlabel("Year")
    plt.ylabel("Frequency")
    plt.title("Distribution of Songs by Year (Rihanna)")
    plt.grid(axis="y", linestyle="--", alpha=0.7)

    plt.savefig("histogram_plot.png")
    plt.show()


if __name__ == "__main__":
    result_df = query_transform()
    result_df.show()
    simple_plot(result_df)
