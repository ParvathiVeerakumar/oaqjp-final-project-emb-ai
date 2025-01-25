# Importing UnitTest of python library
import unittest
# Importing emotion detector method from appliation class
from EmotionDetection.emotion_detection import emotion_detector

# Unit Test Cases Class for testing Emotion Detector
class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detection(self):
        
        # Test Case 1 - Emotion 'Joy'
        result1 = emotion_detector("I am glad this happened")
        self.assertEqual(result1['dominant_emotion'],'joy')

        # Test Case 2 - Emotion 'Anger'
        result2 = emotion_detector("I am really mad about this")
        self.assertEqual(result2['dominant_emotion'],'anger')

        # Test Case 3 - Emotion 'Disgust'
        result3 = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result3['dominant_emotion'],'disgust')

        # Test Case 4 - Emotion 'Sadness'
        result4 = emotion_detector("I am so sad about this")
        self.assertEqual(result4['dominant_emotion'],'sadness')

        # Test Case 5 - Emotion 'Fear'
        result5 = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result5['dominant_emotion'],'fear')

unittest.main()