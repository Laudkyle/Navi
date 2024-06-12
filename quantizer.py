import torch
from transformers import DistilBertForSequenceClassification, DistilBertConfig,DistilBertTokenizer
from sklearn.preprocessing import LabelEncoder
from torch.utils.data import Dataset, DataLoader
from sklearn.model_selection import train_test_split
from tqdm import tqdm
import json, pickle

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Load dataset from JSON file
with open('/intent_dataset.json', 'r') as file:
    dataset = json.load(file)

# Extract labels from the dataset
labels = [sample["answer"] for sample in dataset]

# Use LabelEncoder to convert string labels into integer indices
label_encoder = LabelEncoder()
encoded_labels = label_encoder.fit_transform(labels)

# Save the label encoder to a file using pickle
with open("label_encoder.pkl", 'wb') as le_file:
    pickle.dump(label_encoder, le_file)

# Update the dataset with integer-encoded labels
for i, sample in enumerate(dataset):
    dataset[i]["label"] = encoded_labels[i]

# Split the dataset into training and validation sets
train_data, val_data = train_test_split(dataset, test_size=0.2, random_state=42)

# Define a custom dataset class
class CustomDataset(Dataset):
    def __init__(self, data):
        self.data = data
        self.tokenizer = DistilBertTokenizer.from_pretrained("distilbert-base-uncased")
        self.max_len = 20  # Set the maximum sequence length as needed

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        question = self.data[idx]["question"]
        label = self.data[idx]["label"]

        encoding = self.tokenizer(
            question,
            return_tensors="pt",
            truncation=True,
            padding="max_length",
            max_length=self.max_len,
        )
        input_ids = encoding["input_ids"].squeeze()
        attention_mask = encoding["attention_mask"].squeeze()

        return {"input_ids": input_ids, "attention_mask": attention_mask, "label": torch.tensor(label)}

# Create instances of the custom datasets for training and validation
train_dataset = CustomDataset(train_data)
val_dataset = CustomDataset(val_data)

# Define the dataloaders
train_dataloader = DataLoader(train_dataset, batch_size=2, shuffle=True)
val_dataloader = DataLoader(val_dataset, batch_size=2, shuffle=False)

# Load the pre-trained DistilBERT model
pretrained_model_path = "distil_intent_model"
model = DistilBertForSequenceClassification.from_pretrained(pretrained_model_path).to(device)

# Quantize the model
quantized_model = torch.quantization.quantize_dynamic(
    model,
    {torch.nn.Linear},
    dtype=torch.qint8
)

# Save the quantized model
torch.save(quantized_model.state_dict(), "distil_intent_quantized_model.pth")


