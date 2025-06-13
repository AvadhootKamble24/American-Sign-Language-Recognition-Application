# from flask import Flask, render_template, Response, jsonify
# from detect import generate_frames , get_current_sentence

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/translate')
# def translate():    
#     return render_template('asl_translate.html')

# @app.route('/learn')
# def learn():
#     return render_template('learn_asl.html')

# @app.route('/video_feed')
# def video_feed():
#     return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

# @app.route('/sentence')
# def sentence():
#     s = get_current_sentence()
#     print("⚠️ Returned to frontend:", s)
#     return jsonify(sentence=s)


# @app.route('/end_feed', methods=['POST'])
# def end_feed():
#     # Clean-up logic can go here if needed
#     return ('', 204)
# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, render_template, Response, jsonify
import os

from detect import generate_frames, get_current_sentence

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

@app.route('/learn/alphabet')
def asl_alphabet():
    characters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
    extensions = {}

    for c in characters:
        jpeg_path = f'static/image/alphabet/{c}.jpeg'
        jpg_path = f'static/image/alphabet/{c}.jpg'
        if os.path.exists(jpeg_path):
            extensions[c] = '.jpeg'
        elif os.path.exists(jpg_path):
            extensions[c] = '.jpg'
        else:
            extensions[c] = '.jpg'  # fallback

    return render_template('alphabet.html', characters=characters, extensions=extensions)

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/sentence')
def sentence():
    s = get_current_sentence()
    print("⚠️ Returned to frontend:", s)
    return jsonify(sentence=s)

@app.route('/end_feed', methods=['POST'])
def end_feed():
    return ('', 204)

if __name__ == '__main__':
    app.run(debug=True)
