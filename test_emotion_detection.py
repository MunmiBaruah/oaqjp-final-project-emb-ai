import unittest

from EmotionDetection.emotion_detection import emotion_detector

def test1(self):
    res1 = emotion_detector("I am glad this happened")
    self.assertEqual(res1["dominant_emotion"], "joy")

    res2 = emotion_detector("I am really mad about this")
    self.assertEqual(res1["dominant_emotion"], "anger")

    res3 = emotion_detector("I feel disgusted just hearing about this")
    self.assertEqual(res1["dominant_emotion"], "disgust")

    res4 = emotion_detector("I am so sad about this")
    self.assertEqual(res1["dominant_emotion"], "sadness")

    res5 = emotion_detector("I am really afraid that this will happen")
    self.assertEqual(res1["dominant_emotion"], "fear")

unittest.main()