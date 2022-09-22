# extension-recommendation-engine
Extension Recommendation Engine

## Step 1 : Shrink Dataset
In case the number of extensions (columns) in your dataset is too high, you could shrink the dataset by limiting the number of columns by using `shrink-dataset.py`.
Adjust the values of the following variables in the script as per your needs:
> INPUT_DATASET_FILE_NAME = "dataset-big.csv" <br />
OUTPUT_DATASET_FILE_NAME = "shrinked-dataset.csv"

## Step 2 : Train the model
Train the model by running the script `train-model.py`. The model will be serialized into `model.json`.

## Step 3 : Run the web app
Run the extension recommendation engine by running the script `ext-recommend-app.py`. <br/>
>You could get the extension recommendation from the api: `http://localhost:5000/recommend?installed_extensions=<ext1>,<ext2>`
