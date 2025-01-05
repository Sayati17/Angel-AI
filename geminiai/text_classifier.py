from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
import torch

class textClassifier:
    def __init__(self, model_name: str):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSequenceClassification.from_pretrained(model_name)
        self.classifier = pipeline(
            "text-classification",
            model=self.model,
            tokenizer=self.tokenizer,
            truncation=True,
            max_length=512,
            device=torch.device("cuda" if torch.cuda.is_available() else "cpu"),
        )
    
    def get_classification_score(self, text:str):
        result = self.classifier(text, top_k=None)
        formatted_result = [
            {"label": entry["label"], "score": f"{entry['score']:.5f}"} for entry in result
        ]
        injection_score = next((entry['score'] for entry in formatted_result if entry['label'] == 'INJECTION'), None)
        return int(float(injection_score))