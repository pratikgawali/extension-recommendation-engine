import sys
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

INPUT_DATASET_FILE_NAME = "dataset.csv"

# Read installed extensions data
installed_extensions_data = pd.read_csv(INPUT_DATASET_FILE_NAME, index_col=0)

# Apply cosine similarity -> gives scores on similarity of items
extension_similarity = cosine_similarity(installed_extensions_data.T)
extension_similarity = pd.DataFrame(extension_similarity, index=installed_extensions_data.columns,columns=installed_extensions_data.columns)

# trained model is actually the extension similarity matrix itself
trained_model = extension_similarity.to_json()

# store trained model to a file
original_stdout = sys.stdout # Save a reference to the original standard output
with open('model.json', 'w') as f:
    sys.stdout = f # Change the standard output to the file we created.
    print(trained_model)
    sys.stdout = original_stdout # Reset the standard output to its original
