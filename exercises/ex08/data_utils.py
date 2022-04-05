"""EX08. Dictionary related utility functions."""

__author__ = "730332997"

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Reads the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []
    
    # Open a handle to the data file
    file_handle = open(filename, "r", encoding="utf8")

# Prepare to read the data file as a CSV rather than just strings
    csv_reader = DictReader(file_handle)

# Read each row of the CSV line-by-line
    for row in csv_reader:
        result.append(row) 

    # Close the file when we're done, to free its resources.
    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produces a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table into a column-oriented table."""
    result: dict[str, list[str]] = {}
    
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)

    return result


def head(column_table: dict[str, list[str]], N: int) -> dict[str, list[str]]:
    """Produces a new column-based table with only the first N rows of data for each column."""
    result: dict[str, list[str]] = {}
    for column in column_table:
        chopped_list: list[str] = []
        row_counter = 0
        for row_val in column_table[column]:
            if row_counter < N:
                chopped_list.append(row_val)
                row_counter += 1
        result[column] = chopped_list
    return result


def select(column_table: dict[str, list[str]], wanted_columns: list[str]) -> dict[str, list[str]]:
    """Produces a new column-based table with only a specific subset of the original columns."""
    result: dict[str, list[str]] = {}
    for column_name in column_table:
        if column_name in wanted_columns:
            result[column_name] = column_table[column_name]
    return result


def concat(table_1: dict[str, list[str]], table_2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produces a new column-based table with two column-based tables combined."""
    result: dict[str, list[str]] = {}
    for column_name in table_1:
        result[column_name] = table_1[column_name]
    for cn_2 in table_2:
        if cn_2 in result:
            result[cn_2].extend(table_2[cn_2])
        else:
            result[cn_2] = table_2[cn_2]
    return table_1


def count(input: list[str]) -> dict[str, int]:
    """Given a list, produces a dictionary where each key is a unique value in the given list and each value associated is the number of times that value appeared in the input list."""
    result: dict[str, int] = {}
    for item in input:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result


def average(input: list[str]) -> float:
    """Given a list, converts it into ints and returns the average."""
    total: int = 0
    divisor: int = 0
    output: float = 0
    for item in input:
        total += int(item)
        divisor += 1
    output = round((total / divisor), 2)
    return output


def ratio(list_1: list[str], list_2: list[str]) -> list[float]:
    """Given two lists, converts the values into ints, divides each item on the first list by the respective item on the second list, and returns a list of floats."""
    output: list[float] = []
    i: int = 0
    while i <= len(list_1) - 1:
        output.append(round(int(list_1[i]) / int(list_2[i]), 2))
        i += 1
    return output