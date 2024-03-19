import requests
import json

def emotion_detector(text_to_analyze):
    if not text_to_analyze.strip(): #check if empty
        return None
    url="https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    data={ "raw_document": { "text": text_to_analyze }}
    headers={"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json=data, headers=headers)

    if( response.status_code == 200 ):
        formatted_response = json.loads(response.text)
        emotion_list = formatted_response["emotionPredictions"][0]["emotion"]
        dominant_emotion = max(emotion_list.items(), key=lambda x: x[1])[0]
        return {
            'anger': emotion_list['anger'],
            'disgust': emotion_list['disgust'],
            'fear': emotion_list['fear'],
            'joy': emotion_list['joy'],
            'sadness': emotion_list['sadness'],
            'dominant_emotion': dominant_emotion
        }
    else:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

