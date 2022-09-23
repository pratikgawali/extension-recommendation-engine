from flask import Flask
from flask import request
import pandas as pd

TRAINED_MODEL_FILE_NAME = "model.json"
MAX_NUMBER_OF_RECOMMENDATIONS = 10

# read the trained model to know extension similarity scores
extension_similarity_model = pd.read_json(TRAINED_MODEL_FILE_NAME)

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    return "Hello World!!"

@app.route('/recommend', methods=['GET'])
def recommend_extensions():
    try:
        installed_extensions = request.args.get("installed_extensions").split(',')
        recommended_extensions = get_recommendations(installed_extensions)
        
        result = []
        for extension in recommended_extensions:
            if extension not in installed_extensions:
                result.append(extension)
                if len(result) > MAX_NUMBER_OF_RECOMMENDATIONS:
                    break
            
        return result
    except:
        return "Something went wrong. Please contact admin."

def get_recommendations(installed_extensions):

    similarity_scores_list = pd.DataFrame()
    for extension in installed_extensions:
        similarity_score = pd.DataFrame()
        if extension in extension_similarity_model.index:
            similarity_score = extension_similarity_model[extension]
            similarity_score = similarity_score.sort_values(ascending=False)
        
        similarity_scores_list = similarity_scores_list.append(similarity_score)
    
    # sum the similarity scores for each installed extension & sort to keep the max scored extension first
    similarity_scores_list = similarity_scores_list.sum().sort_values(ascending=False)
    return similarity_scores_list.index

app.run(host="0.0.0.0")