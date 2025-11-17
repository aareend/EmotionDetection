import requests
import json

def emotion_detector(text_to_analyze):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {
        "Content-Type": "application/json",
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    payload = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    try:
        resp_dict = json.loads(response.text)
    except ValueError as e:
        raise RuntimeError("Failed to parse response JSON") from e

    pred_list = resp_dict.get("emotionPredictions", [])
    if not pred_list:
        scores = {k: 0.0 for k in ("anger", "disgust", "fear", "joy", "sadness")}
        dominant = None
    else:
        emotion_block = pred_list[0].get("emotion", {})
        if not emotion_block:
            mentions = pred_list[0].get("emotionMentions", [])
            if mentions and isinstance(mentions, list):
                emotion_block = mentions[0].get("emotion", {})

        scores = {}
        for name in ("anger", "disgust", "fear", "joy", "sadness"):
            try:
                scores[name] = float(emotion_block.get(name, 0.0))
            except (TypeError, ValueError):
                scores[name] = 0.0

        dominant = max(scores, key=scores.get) if any(v is not None for v in scores.values()) else None

    result = {
        "anger": scores["anger"],
        "disgust": scores["disgust"],
        "fear": scores["fear"],
        "joy": scores["joy"],
        "sadness": scores["sadness"],
        "dominant_emotion": dominant
    }

    return result
