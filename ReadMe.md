Here is your complete `README.md` file based on the folder structure and your project description.

---

### ✅ `README.md` (Copy this into your repo)

```markdown
# 🧠 American Sign Language Recognition Application

This project is a deep learning-powered web application that recognizes **American Sign Language (ASL)** gestures using image inputs. Built with **Flask** and **PyTorch**, it provides a simple web interface for real-time or static ASL sign detection.

---

## 📁 Project Structure

```

American Sign Language Recognition Application/
│
├── flask/
│   ├── **pycache**/              # Compiled Python files
│   ├── .history/                 # Editor history (optional)
│   ├── .vscode/                  # VSCode settings
│   ├── static/                   # Static assets (CSS/JS/images)
│   ├── templates/                # HTML templates (Flask/Jinja2)
│   ├── app.py                    # Main Flask app
│   ├── detect.py                 # ASL detection logic
│   ├── best.pt                   # Model checkpoint
│   ├── best\_19\_classes.pt        # Model with 19-class support
│   └── tempCodeRunnerFile.py     # Temporary test script
│
├── Training and models/
│   ├── runs/                     # Model training outputs
│   ├── best\_5.pt                 # Model for 5-class ASL
│   ├── best\_19\_classes.pt        # Model for 19-class ASL
│   └── model.ipynb               # Notebook for training/testing

```

---

## 🚀 Features

- Web-based interface using Flask
- Real-time and image-based ASL detection
- Supports both 5-class and 19-class trained models
- Modular code for easy extension

---

## 🛠️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/AvadhootKamble24/American-Sign-Language-Recognition-Application.git
cd "American Sign Language Recognition Application"
````

### 2. Create and Activate Virtual Environment (Optional)

```bash
python -m venv venv
source venv/bin/activate       # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

> Make sure to create `requirements.txt` if it's not available using `pip freeze > requirements.txt`

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Web App

```bash
cd flask
python app.py
```

Then open your browser and go to `http://127.0.0.1:5000`

---

## 🧠 Available Models

| File Name            | Description                         |
| -------------------- | ----------------------------------- |
| `best.pt`            | Default model (unspecified classes) |
| `best_5.pt`          | Trained on 5 ASL classes            |
| `best_19_classes.pt` | Trained on 19 ASL classes           |

---

## 📓 Training

The `model.ipynb` notebook inside `Training and models/` contains the full training and evaluation pipeline. Model outputs are stored in the `runs/` folder.

---

## 🌐 Future Improvements

* Add webcam support for real-time detection
* Improve UI with responsive design
* Add accuracy charts and confusion matrix
* Deploy the app using Render, HuggingFace Spaces, or Heroku

---

## 📜 License

This project is open-source and available under the [MIT License](LICENSE).

---

## 🙏 Acknowledgements

* PyTorch
* Flask
* OpenCV
* Ultralytics (YOLOv5, if used in training)

```

---

Would you like me to:
- Save this as a downloadable `README.md` file?
- Create a sample `requirements.txt`?
- Add GitHub badges (build, license, etc.) to the top?

Let me know!
```
