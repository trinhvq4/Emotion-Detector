import unittest
from EmotionDetection import emotion_detector


class TestEmotionDetection(unittest.TestCase):
    """Unit test class for emotion detection functionality."""

    def test_output_type(self):
        """Test that the function returns a dictionary."""
        result = emotion_detector("I am happy.")
        self.assertIsInstance(result, dict)

    def test_required_keys_present(self):
        """Test that all required emotion keys exist in the output."""
        result = emotion_detector("I am happy.")
        expected_keys = {
            "anger",
            "disgust",
            "fear",
            "joy",
            "sadness",
            "dominant_emotion"
        }
        self.assertTrue(expected_keys.issubset(result.keys()))

    def test_dominant_emotion_joy(self):
        """Test that a joyful sentence returns joy as dominant emotion."""
        result = emotion_detector("I am extremely happy and excited!")
        self.assertEqual(result["dominant_emotion"], "joy")

    def test_dominant_emotion_sadness(self):
        """Test that a sad sentence returns sadness as dominant emotion."""
        result = emotion_detector("I am very sad and disappointed.")
        self.assertEqual(result["dominant_emotion"], "sadness")

    def test_empty_input(self):
        """Test handling of empty input string."""
        result = emotion_detector("")
        # Depending on implementation, it may return None or an error message
        self.assertTrue(result is None or isinstance(result, dict))

    def test_negative_emotion(self):
        """Test detection of negative emotions like anger or fear."""
        result = emotion_detector("I am angry and frustrated.")
        self.assertIn(result["dominant_emotion"], ["anger", "fear", "sadness", "disgust"])


if __name__ == "__main__":
    unittest.main()
