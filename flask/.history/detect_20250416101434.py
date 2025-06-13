from ultralytics import YOLO
import cv2
from collections import Counter
import requests

# Load trained YOLO model
model = YOLO("best.pt")

# Initialize webcam
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Sentence formation settings
word_counter = Counter()
no_action_frames = 0
max_no_action_frames = 10  # Trigger sentence generation after 10 empty frames

# Groq API Key
GROQ_API_KEY = "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"

# Global variable to store enhanced sentence for live UI display
current_sentence = "Waiting for sentence..."

def filter_and_generate_sentence(counter):
    """
    Forms a sentence from frequently occurring words (count > 1).
    """
    words = [word for word, count in counter.items() if count > 1]
    return " ".join(words).capitalize() if words else None

def enhance_sentence_with_groq(sentence):
    """
    Sends a sentence to the Groq API for grammar improvement.
    """
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    prompt = f"Improve the grammar and structure of this sentence, but respond ONLY with the improved sentence. No explanations: \"{sentence}\""

    payload = {
        "model": "llama3-8b-8192",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 60,
        "temperature": 0.5
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        result = response.json()
        return result["choices"][0]["message"]["content"].strip()
    except requests.exceptions.RequestException as e:
        print(f"❌ API Request failed: {e}")
        return sentence  # fallback to original

def generate_frames():
    """
    Main loop to capture frames, run detection, generate sentences, and yield frames.
    """
    global word_counter, no_action_frames, current_sentence

    while True:
        success, frame = cap.read()
        if not success:
            break

        # Run YOLO model
        results = model(frame, verbose=False)
        current_frame_words = []

        # Extract detected words (class labels)
        for box in results[0].boxes:
            class_index = int(box.cls)
            word = model.names[class_index].lower()
            current_frame_words.append(word)

        # Update word counter or increment idle frame count
        if current_frame_words:
            no_action_frames = 0
            word_counter.update(current_frame_words)
        else:
            no_action_frames += 1

        # Generate sentence if idle frame threshold is reached
        if no_action_frames >= max_no_action_frames:
            sentence = filter_and_generate_sentence(word_counter)
            if sentence:
                print("📝 Raw Sentence:", sentence)
                enhanced_sentence = enhance_sentence_with_groq(sentence)
                if enhanced_sentence:
                    current_sentence = enhanced_sentence
                    print(f"✨ Enhanced Sentence: {current_sentence}")
            word_counter.clear()
            no_action_frames = 0

        # Annotate and stream the frame
        annotated_frame = results[0].plot()
        ret, buffer = cv2.imencode('.jpg', annotated_frame)
        frame_bytes = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

def get_current_sentence():
    """
    Returns the latest generated sentence for display in frontend.
    """
    return current_sentence
