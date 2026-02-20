import requests
import json

def emotion_detector(text_to_analyse):
    """
    Detects emotions from the given text by making a POST request to the Watson NLP API.
    
    Parameters:
        text_to_analyse (str): Input text to analyze emotions.
        
    Returns:
        dict: A dictionary containing the API response.
    """
    # The specified URL for the Watson Emotion Predict service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Required headers specifying the model ID
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    
    # The input text formatted as a JSON object
    input_json = {
        "raw_document": {
            "text": text_to_analyse
        }
    }
    
    try:
        # Send a POST request to the API
        response = requests.post(url, json=input_json, headers=headers)
        
        # Parse and return the JSON response
        return response.json()
        
    except requests.exceptions.RequestException as e:
        return {"error": f"API request failed: {str(e)}"}

# Example standalone execution (for testing)
if __name__ == "__main__":
    sample_text = "I am very happy and excited about this project!"
    output = emotion_detector(sample_text)
    print(json.dumps(output, indent=2))
