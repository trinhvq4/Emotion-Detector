# Import the main application function from the emotion_detection module
from .emotion_detection import application_function

# (Optional) expose emotion_detector as well if required by the project
from .emotion_detection import detect_emotion as emotion_detector

# Define what is available when using: from package import *
__all__ = ["application_function", "emotion_detector"]
