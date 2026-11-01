"""Unit tests for the Watson emotion detector."""
import unittest
from EmotionDetection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Test the five emotion examples specified in the course."""

    def test_joy(self):
        """Check the joy example."""
        self.assertEqual(
            emotion_detector("I am glad this happened")["dominant_emotion"],
            "joy",
        )

    def test_anger(self):
        """Check the anger example."""
        self.assertEqual(
            emotion_detector("I am really mad about this")["dominant_emotion"],
            "anger",
        )

    def test_disgust(self):
        """Check the disgust example."""
        self.assertEqual(
            emotion_detector(
                "I feel disgusted just hearing about this"
            )["dominant_emotion"],
            "disgust",
        )

    def test_sadness(self):
        """Check the sadness example."""
        self.assertEqual(
            emotion_detector("I am so sad about this")["dominant_emotion"],
            "sadness",
        )

    def test_fear(self):
        """Check the fear example."""
        self.assertEqual(
            emotion_detector(
                "I am really afraid that this will happen"
            )["dominant_emotion"],
            "fear",
        )


if __name__ == "__main__":
    unittest.main()
