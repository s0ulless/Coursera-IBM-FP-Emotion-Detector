import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):

    def test_anger(self):
        text = "I am so frustrated and angry right now!"
        result = emotion_detector(text)
        self.assertEqual(result['dominant_emotion'], 'anger')

    def test_disgust(self):
        text = "That was absolutely revolting and disgusting."
        result = emotion_detector(text)
        self.assertEqual(result['dominant_emotion'], 'disgust')

    def test_fear(self):
        text = "I am terrified of walking alone at night."
        result = emotion_detector(text)
        self.assertEqual(result['dominant_emotion'], 'fear')

    def test_joy(self):
        text = "I am so happy and joyful today!"
        result = emotion_detector(text)
        self.assertEqual(result['dominant_emotion'], 'joy')

    def test_sadness(self):
        text = "I feel so sad and depressed."
        result = emotion_detector(text)
        self.assertEqual(result['dominant_emotion'], 'sadness')

if __name__ == '__main__':
    unittest.main()
