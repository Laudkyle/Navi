import torch
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification
from sklearn.preprocessing import LabelEncoder

# Load the trained model
loaded_model = DistilBertForSequenceClassification.from_pretrained("distil_intent_model")

# Load the tokenizer
tokenizer = DistilBertTokenizer.from_pretrained("distilbert-base-uncased")

# Define the label encoder for decoding predictions
label_encoder = LabelEncoder()
label_encoder.classes_ = ["general_functionalities", "location"]  # Update with your classes

# Define the class-to-index mapping
class_to_index = {label: i for i, label in enumerate(label_encoder.classes_)}

# Create a loop for interactive testing
while True:
    # Get user input
    user_input = input("Enter a question (type 'exit' to end): ")

    # Check for exit condition
    if user_input.lower() == 'exit':
        break

    # Tokenize and encode the input
    inputs = tokenizer(user_input, return_tensors="pt", truncation=True, padding="max_length", max_length=20)
    input_ids = inputs["input_ids"]
    attention_mask = inputs["attention_mask"]

    # Make a prediction
    with torch.no_grad():
        outputs = loaded_model(input_ids, attention_mask=attention_mask)
        logits = outputs.logits

    # Get the predicted label
    predicted_label_idx = torch.argmax(logits).item()
    predicted_label = list(class_to_index.keys())[list(class_to_index.values()).index(predicted_label_idx)]

    print(f"Predicted label: {predicted_label}")
