# To include every variable as a possible category for the cardio calories burned, we will create a three-level nested loop
# to iterate over every combination of x, y, and category variables.

# Define all variables including 'Cardio' which represents the cardio calories burned category from Fitbit.
from itertools import permutations

def generate_markdown_table():

    variables = ['Gym', 'Weight', 'Kcals in', 'Kcals out', 'Net Diff', 'Steps', 'Cardio']

    # We use permutations to get all ordered pairs for x and y where x is not equal to y.
    # Then for each pair, we loop over all variables to use as a category, excluding the ones used for x and y.
    variable_combinations = []

    for x, y in permutations(variables, 2):
        for category in variables:
            if category != x and category != y:
                variable_combinations.append((x, y, category))

    # Create a markdown table with all possible combinations
    # Here, we only generate the code to produce the table, we will not print the markdown output as per user request.
    table_header = "| Var 1 | Var 2 | Category | Relationship | Comments |\n| --- | --- | --- | --- | --- |\n"
    table_rows_code = "".join([f"| {comb[0]} | {comb[1]} | {comb[2]} |  |  |\n" for comb in variable_combinations])
    markdown_table_code = table_header + table_rows_code

    # The variable `markdown_table_code` now contains the string with the markdown code for the table.
    # We will not print this output as requested. This code can be used to generate the markdown table.

    # To write the markdown table to a file, we will use Python's file I/O operations.

    # Define the file path where the markdown table will be saved.
    markdown_file_path = '../results/daily_scatterplot_table.md'

    # Write the markdown table code to the file.
    with open(markdown_file_path, 'w') as file:
        file.write(markdown_table_code)

    return markdown_table_code