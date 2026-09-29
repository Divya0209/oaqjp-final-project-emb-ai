from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("EmotionDetector")

@app.route("/emotionDetector")
def emotion_detection():
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] == None:
        return "Invalid text! Please try again!."
        
    # Return a formatted string with the sentiment label and score
    return (f"For the given statement, the system response is 'anger': {response['anger']}, "
    f"'disgust': {response['disgust']}, 'fear': {response['fear']}, 'joy': {response['joy']} and "
    f"'sadness': {response['sadness']}. The dominant emotion is {response['dominant_emotion']}.")

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)