import unittest
from unittest.mock import patch, mock_open
from TextCodeEvaluator import TextCodeEvaluator

class TestTextCodeEvaluator(unittest.TestCase):

    @patch('builtins.open', new_callable=mock_open, read_data='{"url": "example.com", "answers": ["answer1", "answer2"]}\n')
    def test_read_predictions(self, mock_file):
        evaluator = TextCodeEvaluator('mock_predictions.json', 'mock_answers.json')
        expected_result = {"example.com": ["answer1", "answer2"]}
        self.assertDictEqual(evaluator.predictions, expected_result)

    @patch('builtins.open', new_callable=mock_open, read_data='{"url": "example.com", "idx": "answer1"}\n')
    def test_read_answers(self, mock_file):
        evaluator = TextCodeEvaluator('mock_predictions.json', 'mock_answers.json')
        expected_result = {"example.com": "answer1"}
        self.assertDictEqual(evaluator.answers, expected_result)

    @patch('builtins.open', new_callable=mock_open)
    def test_mrr(self, mock_file):
        evaluator = TextCodeEvaluator('mock_predictions.json', 'mock_answers.json')
        evaluator.predictions = {"example.com": ["answer1", "answer2"]}
        evaluator.answers = {"example.com": "answer1"}
        self.assertEqual(evaluator.mrr(), 1.0)

    @patch('builtins.open', new_callable=mock_open)
    def test_web_accuracy(self, mock_file):
        evaluator = TextCodeEvaluator('mock_predictions.json', 'mock_answers.json')
        evaluator.predictions = {"example.com": ["answer1", "answer2"]}
        evaluator.answers = {"example.com": "answer1"}
        self.assertEqual(evaluator.web_accuracy(), 1.0)

    @patch('builtins.open', new_callable=mock_open)
    def test_calculate_em(self, mock_file):
        evaluator = TextCodeEvaluator('mock_predictions.json', 'mock_answers.json')
        evaluator.predictions = {"example.com": ["answer1", "answer2"]}
        evaluator.answers = {"example.com": "answer1"}
        self.assertEqual(evaluator.calculate_em(), 1.0)

    @patch('builtins.open', new_callable=mock_open)
    def test_calculate_bleu(self, mock_file):
        evaluator = TextCodeEvaluator('mock_predictions.json', 'mock_answers.json')
        evaluator.predictions = {"example.com": ["answer1", "answer2"]}
        evaluator.answers = {"example.com": "answer1"}
        score = evaluator.calculate_bleu()
        self.assertTrue(0 <= score <= 1)


if __name__ == '__main__':
    unittest.main()
