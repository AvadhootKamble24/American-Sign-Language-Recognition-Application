from flask import Flask, render_template, Response, jsonify
from detect import generate_frames , get_current_sentence

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate')
def translate():
    return render_template('asl_translate.html')

@app.route('/learn')
def learn():
    return render_template('learn_asl.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/sentence')
def sentence():
    return jsonify(sentence=get_current_sentence())

def get_current_sentence():
    # Placeholder implementation for demonstration
    return "This is a sample sentence."

@app.route('/end_feed', methods=['POST'])
def end_feed():
    # Clean-up logic can go here if needed
    return ('', 204)
if __name__ == '__main__':
    app.run(debug=True)
