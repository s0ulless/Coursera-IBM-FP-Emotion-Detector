import requests
import json

# 2a
##def emotion_detector(text_to_analyze):
##    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
##    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
##    input_json = { "raw_document": { "text": text_to_analyze } }
##    formatted_response = json.loads(response.text)
##
##    return formatted_response

#3a
##def emotion_detector(text_to_analyze):
##    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
##    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
##    input_json = { "raw_document": { "text": text_to_analyze } }
##    response = requests.post(URL, json=input_json, headers=header)
##    formatted_response = json.loads(response.text)
##
##    # Extract emotion scores
##    emotions = formatted_response.get("emotionPredictions", [])[0].get("emotion", {})
##
##    anger_score = emotions.get("anger", 0)
##    disgust_score = emotions.get("disgust", 0)
##    fear_score = emotions.get("fear", 0)
##    joy_score = emotions.get("joy", 0)
##    sadness_score = emotions.get("sadness", 0)
##
##    # Determine dominant emotion
##    scores = {
##        'anger': anger_score,
##        'disgust': disgust_score,
##        'fear': fear_score,
##        'joy': joy_score,
##        'sadness': sadness_score
##    }
##    dominant_emotion = max(scores, key=scores.get)
##
##    return {
##        'anger': anger_score,
##        'disgust': disgust_score,
##        'fear': fear_score,
##        'joy': joy_score,
##        'sadness': sadness_score,
##        'dominant_emotion': dominant_emotion
##    }

# 7a
def emotion_detector(text_to_analyze):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(URL, json=input_json, headers=header)

    # Handle blank input or bad request
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    formatted_response = json.loads(response.text)

    # Extract emotion scores
    emotions = formatted_response.get("emotionPredictions", [])[0].get("emotion", {})

    anger_score = emotions.get("anger", 0)
    disgust_score = emotions.get("disgust", 0)
    fear_score = emotions.get("fear", 0)
    joy_score = emotions.get("joy", 0)
    sadness_score = emotions.get("sadness", 0)

    scores = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }

    dominant_emotion = max(scores, key=scores.get)

    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }
