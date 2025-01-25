# Import Flask, render_template, request from the flask framework package :
from flask import Flask, render_template, request
# Import the emotion_detector function from the package created:
from EmotionDetection.emotion_detection import emotion_detector

# Instatiating Flask Class
app = Flask ("Emotion Detector")

@app.route("/emotionDetector")
def emot_detector():
    text_to_analyze=request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    resultString = ""
    for key,value in response.items():
        if key=='joy':
            resultString+=f"'{key}': {value} and "
        elif key=='sadness':
            resultString+=f"'{key}': {value}. "
        elif key=='dominant_emotion':
            resultString+=f"The dominant emotion is <strong>{value}</strong>"
        else:
            resultString+=f"'{key}': {value}, "
    return f"For the given statement, the system response is {resultString}"

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0",port="5000")