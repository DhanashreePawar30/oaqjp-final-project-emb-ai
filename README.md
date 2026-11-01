# Final project

IBM AI-Based Web Application Development and Deployment — Emotion Detector.

## Setup (run in Skills Network Theia Lab)

```bash
python3 -m pip install requests flask
python3 -m pip install pylint
```

Run tests:
```bash
python3 -m unittest -v test_emotion_detection.py
```

Start Flask:
```bash
python3 server.py
```

Run static analysis:
```bash
pylint server.py
```

Important: The Watson EmotionPredict API is hosted for the Skills Network environment. Follow the course instruction to run this project in Theia Lab; it may not be accessible from a local VS Code terminal.
