import requests # Import the requests library to handle HTTP requests
import json # Import the json library to convert the response to a dictionary

def emotion_detector(text_to_analyze): # This function takes string input
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict' #URL of emotion detection fuction
    myobj =  { "raw_document": { "text": text_to_analyze } } # Dictionary with text to analyze
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"} # Headers required for API request
    response = requests.post(url, json = myobj, headers=header)  # Send a POST request to the API with the text and headers
    
    if response.status_code == 400:
        return {
            'anger' : None,
            'disgust': None,
            'fear': None,
            'joy' : None, 
            'sadness' : None,
            'dominant_emotion' : None
        }

    formatted_response = json.loads(response.text) # response text passed as argument to json
  
    # Extract the emotion label and score 
    emotion_predictions = formatted_response['emotionPredictions'][0]['emotion']
    # Finding the dominant emotion based on the score
    dominant_emotion = max(emotion_predictions.items(), key=lambda item: item[1])[0]
    #Create a new ey value with the dominant emotion
    emotion_predictions['dominant_emotion'] = dominant_emotion
    return emotion_predictions