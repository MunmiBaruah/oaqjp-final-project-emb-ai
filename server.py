from flask import Flask, request, jsonify, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def get_emotion():
    return render_template("index.html")

@app.route("/emotionDetector")
def sent_detector():
    text_to_analyze = request.args.get('textToAnalyze')
    emotions = emotion_detector(text_to_analyze)

    if emotions is None:
        return "Invalid text! Please try again!."
    else:
        return "The given text has been identified as {}.".format(emotions)

if __name__ == "__main__":
    app.run(debug=True)
