import csv
import pandas as pd

INPUT_DATASET_FILE_NAME = "dataset-full-final.csv"
OUTPUT_DATASET_FILE_NAME = "shrinked-dataset.csv"

EXTENSION_LIMIT_COUNT = 5000

original_data = pd.read_csv(INPUT_DATASET_FILE_NAME, header=None)

# limit the number of columns
shrinked_data = original_data.iloc[:,:EXTENSION_LIMIT_COUNT].values.tolist() 

output_data = []
for data in shrinked_data:
    output_data.append(data)

with open(OUTPUT_DATASET_FILE_NAME, "w", encoding='UTF8', newline='') as my_csv:
    csvWriter = csv.writer(my_csv)
    csvWriter.writerows(output_data)

print("Success!")