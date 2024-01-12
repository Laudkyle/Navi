import numpy as np
from tensorflow.keras.models import load_model
import pickle
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer

# Load the saved model
model = load_model("direction_model.h5")

# Load the tokenizer
with open('tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)

# Load the direction labels
with open('direction_labels.pickle', 'rb') as handle:
    direction_labels = pickle.load(handle)

# Function to preprocess input text and make predictions
def predict_direction(input_text, tokenizer, max_sequence_length):
    # Tokenize the text
    tokenized_text = tokenizer.texts_to_sequences([input_text])

    # Pad the sequence
    padded_text = pad_sequences(tokenized_text, maxlen=max_sequence_length)

    # Make predictions
    predictions = model.predict(padded_text)

    # Get the predicted direction label
    predicted_label = direction_labels[np.argmax(predictions)]

    return predicted_label

# Example usage
input_question = "What's in my hand?"
max_sequence_length = 9  # Replace with the actual max_sequence_length used during training
predicted_direction = predict_direction(input_question, tokenizer, max_sequence_length)
print(f"Predicted Direction: {predicted_direction}")
