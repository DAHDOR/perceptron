import unittest as ut
from perceptron import Perceptron

class TestPerceptron(ut.TestCase):

    def setUp(self):
        self.perceptron = Perceptron(input_size=2, learning_rate=0.1)

    def test_initial_weights(self):
        weights = self.perceptron.weights
        self.assertEqual(len(weights), 2)
        self.assertTrue(all(weight == 0 for weight in weights))

    def test_training(self):
        training_data = [[0, 0], [0, 1], [1, 0], [1, 1]]
        labels = [0, 0, 0, 1]
        self.perceptron.train(training_data, labels, epochs=10)
        predictions = [self.perceptron.predict(data) for data in training_data]
        self.assertEqual(predictions, labels)

    def test_prediction(self):
        self.perceptron.weights = [0.5, -0.5]  # Setting weights for testing
        prediction = self.perceptron.predict([1, 1])
        self.assertEqual(prediction, 1)

if __name__ == '__main__':
    ut.main()