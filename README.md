# Emotion Detection Web Application

This project is a Python-based **Emotion Detection** application that uses IBM Watson NLP to analyze emotions in text.  
It includes a custom Python package, a Flask API server, and automated unit tests.


## Features

- Detects five core emotions:
  - **anger**
  - **disgust**
  - **fear**
  - **joy**
  - **sadness**
- Identifies the **dominant emotion**.
- Provides a REST API endpoint at `/emotionDetector`.
- Supports both **GET** and **POST** methods.
- Handles invalid or blank input gracefully.
- Fully tested with Python's `unittest`.
  

---

## How to Run the Flask Server

Start the application with:

```bash
python3 server.py
```
The server will start at:

http://127.0.0.1:5000

## API Usage

GET Request

Use your browser or curl:

http://127.0.0.1:5000/emotionDetector?text=I%20love%20my%20life

POST Request
```
curl -X POST -H "Content-Type: application/json" \
     -d '{"text": "I think I am having fun"}' \
     http://127.0.0.1:5000/emotionDetector
```
## Sample Output

For the given statement, the system response is 'anger': 0.01,
'disgust': 0.00, 'fear': 0.01, 'joy': 0.95 and 'sadness': 0.04.
The dominant emotion is joy.

## Running Unit Tests
```
python3 test_emotion_detection.py
```

You should see all tests pass successfully.
