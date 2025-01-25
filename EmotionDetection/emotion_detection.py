# Importing python libraries requests
import requests
import json

#Function to get emotion detection
#Using Emotion Predict from watson NLP Library
def emotion_detector(text_to_analyze):

    #EndPoint URL and Headers for service request
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # parsing the text passed as argument to the function
    input_json = { "raw_document": { "text": text_to_analyze } }

    # POST request call to Emotion Predict Service from Watson NLP Library
    # Storing response as received from the Emotion Detection function
    response = requests.post(url, json=input_json, headers=header)

    # Converting text attribute of response to json
    formatted_response = json.loads(response.text)
    # Storing emotions and its scores from the response to a dictionary variable
    emotion_dict = formatted_response['emotionPredictions'][0]['emotion']

    # Calculating dominant emotion by comparing emotion scores
    dominant_emotion = None
    dominant_emotion_score = 0

    for key, value in emotion_dict.items():
        if value>=dominant_emotion_score:
            dominant_emotion_score = value
            dominant_emotion = key
    # Appending the Dominant emotion to the dictionary as mentioned
    emotion_dict['dominant_emotion'] = dominant_emotion
    # Returning the emotion dictionary created
    return emotion_dict