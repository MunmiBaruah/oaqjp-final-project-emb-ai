import requests

def emotion_detector(text_to_analyze):
    if not text_to_analyze.strip(): #check if empty
        return None
    url="https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    data={ "raw_document": { "text": text_to_analyze }}
    headers={"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 200:
        return response.text
    else:
        return ""
