"""
Final project: AI-Based Web Application Development and Deployment
"""
# Import flask, request and render_template from flask
from flask import Flask, request, render_template

# Import emotion_detector from EmotionDetection
from EmotionDetection.emotion_detection import emotion_detector

# Initiate the flask app
app = Flask(__name__)

@app.route("/")
def get_emotion():
    """ Render index.html template in the base url """
    return render_template("index.html")

@app.route("/emotionDetector")
def sent_detector():
    """ emotion detector """
    text_to_analyze = request.args.get('textToAnalyze')
    emotions = emotion_detector(text_to_analyze)
    if emotions is None:
        return "Invalid text! Please try again!."
    return "The given text has been identified as {}.".format(emotions)

if __name__ == "__main__":
    app.run(debug=True)
