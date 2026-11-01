"""Flask web application for Watson NLP emotion detection."""
from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

APP = Flask(__name__)


@APP.route("/")
def render_index_page():
    """Render the home page."""
    return render_template("index.html")


@APP.route("/emotionDetector")
def emotion_detector_route():
    """Analyze text supplied in the textToAnalyze query parameter."""
    text_to_analyze = request.args.get("textToAnalyze", "")
    result = emotion_detector(text_to_analyze)

    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    return (
        "For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )


if __name__ == "__main__":
    APP.run(host="0.0.0.0", port=5000)
