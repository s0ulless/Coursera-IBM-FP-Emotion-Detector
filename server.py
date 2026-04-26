##from flask import Flask, request, jsonify, render_template
##from EmotionDetection.emotion_detection import emotion_detector
##
####app = Flask("Final Proj Emo Detector")
####
####@app.route('/')
####def index():
####    # Serve index.html from /templates
####    return render_template('index.html')
####
####@app.route('/emotionDetector', methods=['GET', 'POST'])
####def detect_emotion():
####    if request.method == 'GET':
####        text_to_analyze = request.args.get('textToAnalyze', '')
####    else:  # POST
####        data = request.get_json()
####        text_to_analyze = data.get('text', '')
####
####    result = emotion_detector(text_to_analyze)
####    return jsonify(result)
####
####if __name__ == '__main__':
####    app.run(host='0.0.0.0', port=5000, debug=True)
##
### 7b
####from flask import Flask, request, jsonify, render_template
####from EmotionDetection.emotion_detection import emotion_detector
####
####app = Flask("Final Proj Emo Detector")
####
####@app.route('/')
####def index():
####    return render_template('index.html')
####
####@app.route('/emotionDetector', methods=['GET', 'POST'])
####def detect_emotion():
####    # Handle GET (query parameter) and POST (JSON body)
####    if request.method == 'GET':
####        text_to_analyze = request.args.get('textToAnalyze', '')
####    else:  # POST
####        data = request.get_json()
####        text_to_analyze = data.get('text', '')
####
####    result = emotion_detector(text_to_analyze)
####
####    # Error handling: if dominant_emotion is None, return error message
####    if result['dominant_emotion'] is None:
####        return jsonify({"message": "Invalid text! Please try again!"})
####
####    return jsonify(result)
####
####if __name__ == '__main__':
####    app.run(host='0.0.0.0', port=5000, debug=True)

# Pylint-compliant
"""
Server code
"""
from flask import Flask, request, jsonify, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Final Proj Emo Detector")

@app.route('/')
def index():
    """
    Renders index.html
    """
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET', 'POST'])
def detect_emotion():
    """
    Handle GET (query parameter) and POST (JSON body)
    """
    if request.method == 'GET':
        text_to_analyze = request.args.get('textToAnalyze', '')
    else:  # POST
        data = request.get_json()
        text_to_analyze = data.get('text', '')

    result = emotion_detector(text_to_analyze)

    # Error handling: if dominant_emotion is None, return error message
    if result['dominant_emotion'] is None:
        return jsonify({"message": "Invalid text! Please try again!"})

    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
