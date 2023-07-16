import json
import logging
import numpy as np
from sklearn.metrics import accuracy_score
from nltk.translate.bleu_score import corpus_bleu


class TextCodeEvaluator:
    def __init__(self, predictions_file, ground_truth_file):
        self.predictions = self.read_predictions(predictions_file)
        self.answers = self.read_answers(ground_truth_file)

    def benchmark(self, metrics):
        results = {}
        for metric in metrics:
            if hasattr(self, metric):
                results[metric] = getattr(self, metric)()
            else:
                logging.error(f"Unsupported metric: {metric}")
        return results

    def mrr(self):
        scores = []
        for key in self.answers:
            if key not in self.predictions:
                logging.error("Missing prediction for url {}.".format(key))
                continue
            flag = False
            for rank, idx in enumerate(self.predictions[key]):
                if idx == self.answers[key]:
                    scores.append(1 / (rank + 1))
                    flag = True
                    break
            if not flag:
                scores.append(0)
        return round(np.mean(scores), 4)

    def web_accuracy(self):
        y_trues, y_preds = [], []
        for key in self.answers:
            if key not in self.predictions:
                logging.error("Missing prediction for url {}.".format(key))
                continue
            y_trues.append(self.answers[key])
            y_preds.append(self.predictions[key][0])  # Assuming single prediction per key
        return accuracy_score(y_trues, y_preds)

    def calculate_em(self):
        em = 0.0
        for key in self.answers:
            if self.predictions[key][0].split() == self.answers[key].split():
                em += 1
        return em / len(self.answers)

    def calculate_bleu(self):
        references = [ans.split() for ans in self.answers.values()]
        candidates = [pred[0].split() for pred in self.predictions.values()]
        bleu_score = corpus_bleu(references, candidates)
        return bleu_score

    def read_predictions(self, filename):
        predictions = {}
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                js = json.loads(line)
                predictions[js.get('url')] = js.get('answers')
        return predictions

    def read_answers(self, filename):
        answers = {}
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                js = json.loads(line)
                answers[js.get('url')] = js.get('idx')
        return answers
