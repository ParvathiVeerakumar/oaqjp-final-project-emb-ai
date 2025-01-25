''' Import the emotion_detector function from the package created 
    and Import Flask, render_template, request 
    from the flask framework package
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Instatiating Flask Class
app = Flask ("Emotion Detector")

@app.route("/emotionDetector")
def emot_detector():
    """ This code receives the text from the HTML interface and 
        runs emotion analysis over it using emotion_detection()
        function. The output returned shows the label and its emotions 
        score, dominant emotion for the provided text.
    """
    text_to_analyze=request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!."
    result_string = ""
    for key,value in response.items():
        if key=='joy':
            result_string+=f"'{key}': {value} and "
        elif key=='sadness':
            result_string+=f"'{key}': {value}. "
        elif key=='dominant_emotion':
            result_string+=f"The dominant emotion is <strong>{value}</strong>"
        else:
            result_string+=f"'{key}': {value}, "
    return f"For the given statement, the system response is {result_string}"

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0",port="5000")
