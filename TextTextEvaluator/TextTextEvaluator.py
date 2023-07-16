import json
import logging
import numpy as np
from sklearn.metrics import accuracy_score
from nltk.translate.bleu_score import corpus_bleu

class TextTextEvaluator:
    def __init__(self, predictions_file, ground_truth_file):
        self.predictions = self.read_predictions(predictions_file)
        self.answers = self.read_answers(ground_truth_file)

    def calculate_bleu(self):
        references = [ans.split() for ans in self.answers.values()]
        candidates = [pred[0].split() for pred in self.predictions.values()]
        bleu_score = corpus_bleu(references, candidates)
        return bleu_score
