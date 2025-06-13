# American Sign Language Recognition Application 🧠🤟

This project is a deep learning-based web application that can recognize American Sign Language (ASL) gestures from real-time images or video. The application is built with **Flask** and leverages **pre-trained PyTorch models** to detect and classify ASL signs.

---

## 📂 Project Structure

American Sign Language Recognition Application/
│
├── flask/
│ ├── pycache/ # Compiled Python files
│ ├── .history/ # Editor history (optional in Git)
│ ├── .vscode/ # VSCode settings
│ ├── static/ # Static files (CSS, JS, images)
│ ├── templates/ # HTML templates (Jinja2)
│ ├── app.py # Main Flask app entry point
│ ├── detect.py # ASL detection logic
│ ├── best.pt # Model checkpoint
│ ├── best_19_classes.pt # Model with 19-class support
│ └── tempCodeRunnerFile.py # Temporary script (can ignore)
│
├── Training and models/
│ ├── runs/ # Training output folder (e.g., YOLO/runs/)
│ ├── best_5.pt # Model trained on 5 ASL classes
│ ├── best_19_classes.pt # Model trained on 19 ASL classes
│ └── model.ipynb # Training and evaluation notebook


---

## 🚀 Features

- Real-time ASL sign detection using PyTorch
- Web interface with Flask backend
- Support for multiple model versions (5 and 19 class classifiers)
- Modular and clean directory structure

---

## 🛠️ Installation

1. **Clone the repo**
```bash
git clone https://github.com/AvadhootKamble24/American-Sign-Language-Recognition-Application.git
cd American-Sign-Language-Recognition-Application

2. **Create a virtual environment (optional but recommended)**

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. **Install dependencies**

pip install -r requirements.txt
(Create a requirements.txt using pip freeze > requirements.txt if not already present.)


▶️ *Run the Flask App*

cd flask
python app.py
Then open your browser and navigate to http://127.0.0.1:5000

📊 Models
-best.pt: Default trained model

-best_5.pt: Model trained on 5 ASL gestures

-best_19_classes.pt: Model trained on 19 gestures for broader recognition