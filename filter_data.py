import csv
import random

def filter_rows(input_file, output_file, condition):
    with open(input_file, "r") as infile, open(output_file, "w", newline="") as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        header = next(reader)
        writer.writerow(header)

        for row in reader:
            if condition(row):
                writer.writerow(row)

def select_random_rows(input_file, output_file, num_rows, columns=None):
    with open(input_file, "r") as infile, open(output_file, "w", newline="") as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        header = next(reader)
        if columns:
            writer.writerow([header[i] for i in columns])
        else:
            writer.writerow(header)

        data_rows = [row for row in reader]
        random.shuffle(data_rows)

        for i in range(min(num_rows, len(data_rows))):
            if columns:
                writer.writerow([data_rows[i][j] for j in columns])
            else:
                writer.writerow(data_rows[i])


# STEP 1 : Filter data by excluding null values
filter_rows("dataset.csv", "filter_nulls.csv", lambda row: "Overall" not in row and "~" not in row)

# STEP 2 : Filter Data by White Male, Hispanic Female
filter_rows("data_full/filter_nulls.csv", "data_full/population_1.csv", lambda row: row[13] == "Male" and row[15] == "White")
filter_rows("data_full/filter_nulls.csv", "data_full/population_2.csv", lambda row: row[13] == "Female" and row[15] == "Hispanic")

#STEP 3 : Grab 30 random rows from each population
select_random_rows("data_full/population_1.csv", "data_30/30_random_columns_population1.csv", 30, columns=[13, 15, 7])
select_random_rows("data_full/population_2.csv", "data_30/30_random_columns_population2.csv", 30, columns=[13, 15, 7])
