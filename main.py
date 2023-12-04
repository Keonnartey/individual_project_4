"""
Main cli or app entry point
"""

from mylib.extract import extract
from mylib.transform import load
from mylib.query_viz import query_transform, simple_plot
import os

ma


if __name__ == "__main__":
    current_directory = os.getcwd()
    print(current_directory)
    extract()
    result_df = query_transform()
    result_df.show()
    simple_plot(result_df)
    load()
