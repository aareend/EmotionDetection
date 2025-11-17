"""Flask server exposing an emotion detection endpoint."""

from flask import Flask, Response, request
from EmotionDetection import emotion_detector

HOST = "127.0.0.1"
PORT = 5000
ENDPOINT = "/emotionDetector"
METHODS = ["GET", "POST"]

app = Flask(__name__)


@app.route(ENDPOINT, methods=METHODS)
def emotionDetector():  # pylint: disable=invalid-name
    """Handle requests to the emotion detection endpoint."""

    if request.method == "POST" and request.is_json:
        data = request.get_json()
        text = data.get("text") if isinstance(data, dict) else None
    else:
        text = request.args.get("text")

    if text is None:
        return Response(
            "Missing 'text' parameter (provide via JSON POST {\"text\": \"...\"}"
            " or ?text=... in GET)",
            status=400,
            mimetype="text/plain",
        )

    try:
        result = emotion_detector(text)
    except Exception as exc:  # pylint: disable=broad-exception-caught
        return Response(f"Error processing text: {exc}", status=500, mimetype="text/plain")

    anger = result.get("anger")
    disgust = result.get("disgust")
    fear = result.get("fear")
    joy = result.get("joy")
    sadness = result.get("sadness")
    dominant = result.get("dominant_emotion")

    if dominant is None:
        return Response("Invalid text! Please try again!", mimetype="text/plain")

    response_text = (
        "For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. The dominant emotion is {dominant}."
    )

    return Response(response_text, mimetype="text/plain")


if __name__ == "__main__":
    app.run(host=HOST, port=PORT)
