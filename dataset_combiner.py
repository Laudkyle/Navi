import json

dataset_list = ['dataset_activate_functionalities.json', 'dataset_battery.json', 'dataset_functionalities.json', 'dataset_general_knowledge.json', 'dataset_idle_functionalities.json', 'dataset_location.json', 'dataset_name.json', 'dataset_navigation_functionalities.json', 'dataset_reading_functionalities.json']

combined_dataset = []

# Loop through the dataset_list and load each dataset
for dataset_file in dataset_list:
    with open(dataset_file, 'r') as file:
        current_dataset = json.load(file)
        combined_dataset += current_dataset

# Save the combined dataset to a JSON file
with open('intent_dataset.json', 'w') as json_file:
    json.dump(combined_dataset, json_file, indent=2)

print("Combined dataset saved to env/combined_dataset.json")
