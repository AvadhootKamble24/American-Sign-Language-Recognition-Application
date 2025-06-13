from ultralytics import YOLO
import cv2
from collections import Counter
import requests

# Initialize YOLO model
model = YOLO("best.pt")

# Setup video capture
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Sentence formation configuration
word_counter = Counter()
no_action_frames = 0
max_no_action_frames = 10  # Number of frames with no detection before sentence generation

# Groq API Key (replace with your actual key)
GROQ_API_KEY = "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"

def filter_and_generate_sentence(counter):
    """
    Returns a sentence formed from words that appeared more than once.
    """
    words = [word for word, count in counter.items() if count > 1]
    return " ".join(words).capitalize() if words else None

def enhance_sentence_with_groq(sentence):
    """
    Sends the generated sentence to the Groq API for grammar improvement.
    """
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    prompt = f"Improve the grammar and structure of this sentence, but respond ONLY with the improved sentence. No explanations: \"{sentence}\""

    payload = {
        "model": "llama3-8b-8192",  # Example model, use your appropriate model
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
        data = response.json()
        return data["choices"][0]["message"]["content"].strip()
    except requests.exceptions.RequestException as e:
        print(f"❌ API Request failed: {e}")
        return None

def generate_frames():
    global word_counter, no_action_frames

    while True:
        success, frame = cap.read()
        if not success:
            break

        results = model(frame, verbose=False)
        current_frame_words = []

        # Extract detected class names from YOLO results
        for box in results[0].boxes:
            class_index = int(box.cls)
            word = model.names[class_index].lower()
            current_frame_words.append(word)

        # Update word counter or increment 'no action' counter
        if current_frame_words:
            no_action_frames = 0
            word_counter.update(current_frame_words)
        else:
            no_action_frames += 1

        # If enough idle frames have passed, form a sentence
        if no_action_frames >= max_no_action_frames:
            sentence = filter_and_generate_sentence(word_counter)
            if sentence:
                print("📝 Raw Sentence:", sentence)
                # Enhance the sentence via API
                enhanced_sentence = enhance_sentence_with_groq(sentence)
                if enhanced_sentence:
                    print(f"✨ Enhanced Sentence: {enhanced_sentence}")
            word_counter.clear()
            no_action_frames = 0

        # Encode and yield the annotated frame for web streaming or display
        annotated_frame = results[0].plot()
        ret, buffer = cv2.imencode('.jpg', annotated_frame)
        frame_bytes = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')
