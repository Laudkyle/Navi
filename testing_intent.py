import torch
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification
from sklearn.preprocessing import LabelEncoder
import json

# Load the pre-trained model
model = DistilBertForSequenceClassification.from_pretrained("distil_intent_model")
tokenizer = DistilBertTokenizer.from_pretrained("distilbert-base-uncased")

# Load dataset from JSON file
with open('/datasets/intent_dataset.json', 'r') as file:
    dataset = json.load(file)

# Extract labels from the dataset
labels = [sample["answer"] for sample in dataset]

# Use LabelEncoder to convert string labels into integer indices
label_encoder = LabelEncoder()
encoded_labels = label_encoder.fit_transform(labels)

# Manually input questions for predictions
while True:
    # Manually type a question
    input_question = input("Type your question (or 'exit' to end): ")

    # Check if the user wants to exit
    if input_question.lower() == 'exit':
        break

    # Tokenize and encode the input question
    input_ids = tokenizer(input_question, return_tensors="pt", truncation=True, padding=True)["input_ids"]

    # Make predictions
    with torch.no_grad():
        model.eval()
        logits = model(input_ids).logits

    # Convert logits to predicted labels
    predicted_label = torch.argmax(logits, dim=1).item()
    predicted_label = label_encoder.inverse_transform([predicted_label])[0]

    # Print the predicted label
    print(f"Predicted Label for '{input_question}': {predicted_label}")
