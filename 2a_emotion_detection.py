from ibm_watson_nlp import EmotionPredict


# Load the pretrained Watson NLP emotion model (English)
# Make sure the model is downloaded locally or available in your environment
# Example model: emotion_aggregated-workflow_lang_en_stock
try:
    emotion_model = EmotionPredict.load("emotion_aggregated-workflow_lang_en_stock")
except Exception as e:
    raise RuntimeError(
        "Failed to load Watson NLP Emotion model. "
        "Ensure the model is installed and the path is correct."
    ) from e


def detect_emotion(text: str) -> dict:
    """
    Detect emotions from the given text using Watson NLP.

    Parameters:
        text (str): Input text to analyze emotions.

    Returns:
        dict: A dictionary containing emotion scores and dominant emotion.
    """
    if not text or not isinstance(text, str):
        return {
            "error": "Invalid input. Please provide a non-empty string."
        }

    try:
        # Run emotion prediction
        result = emotion_model.predict(text)

        # Extract emotion scores
        emotions = {
            "anger": result.emotion.get("anger", 0.0),
            "disgust": result.emotion.get("disgust", 0.0),
            "fear": result.emotion.get("fear", 0.0),
            "joy": result.emotion.get("joy", 0.0),
            "sadness": result.emotion.get("sadness", 0.0),
        }

        # Determine dominant emotion
        dominant_emotion = max(emotions, key=emotions.get)

        # Application-level response format
        response = {
            "input_text": text,
            "emotions": emotions,
            "dominant_emotion": dominant_emotion,
            "status": "success"
        }

        return response

    except Exception as e:
        return {
            "error": f"Emotion detection failed: {str(e)}",
            "status": "failed"
        }


def application_function(text: str) -> dict:
    """
    Main application function for the Emotion Detection App.
    This function is designed to be called by UI, API, or other modules.

    Parameters:
        text (str): User input text.

    Returns:
        dict: Structured emotion analysis result.
    """
    result = detect_emotion(text)

    # Additional application-level formatting (if needed)
    if "error" in result:
        return {
            "application": "Emotion Detector",
            "result": result,
            "code": 400
        }

    return {
        "application": "Emotion Detector",
        "result": result,
        "code": 200
    }


# Example standalone execution (for testing)
if __name__ == "__main__":
    sample_text = "I am very happy and excited about this project!"
    output = application_function(sample_text)
    print(output)
