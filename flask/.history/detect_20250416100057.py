from ultralytics import YOLO
import cv2
from collections import Counter

model = YOLO(r"best.pt")
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

word_counter = Counter()
no_action_frames = 0
max_no_action_frames = 10
sentence_output = ""

def filter_and_generate_sentence(counter):
    words = [word for word, count in counter.items() if count > 1]
    return " ".join(words).capitalize() if words else None

def generate_frames():
    global word_counter, no_action_frames, output_text
    while True:
        success, frame = cap.read()
        if not success:
            break

        results = model(frame, verbose=False)
        current_frame_words = []

        for box in results[0].boxes:
            class_index = int(box.cls)
            word = model.names[class_index].lower()
            current_frame_words.append(word)

        if current_frame_words:
            no_action_frames = 0
            word_counter.update(current_frame_words)
        else:
            no_action_frames += 1

        if no_action_frames >= max_no_action_frames:
            sentence = filter_and_generate_sentence(word_counter)
            if sentence:
                output_text = sentence
                print("Output Sentence:", output_text)
            word_counter.clear()
            no_action_frames = 0

        annotated_frame = results[0].plot()
        ret, buffer = cv2.imencode('.jpg', annotated_frame)
        frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')