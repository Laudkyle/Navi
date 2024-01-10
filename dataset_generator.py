import json

def transform_to_json(questions, output_file):
    json_data = []

    for index, question in enumerate(questions, start=1):
        json_entry = {
            "question": question,
            "answer": f"battery_health"
        }
        json_data.append(json_entry)

    with open(output_file, 'w') as file:
        json.dump(json_data, file, indent=2)

questions = [
    "How much battery do you have left?",
    "Can you tell me your current battery level?",
    "What is your remaining battery percentage?",
    "Could you inform me about your battery status?",
    "In terms of power, where do you stand?",
    "What is your current battery level?",
    "Can you disclose your remaining battery percentage?",
    "How is your battery holding up?",
    "What's the status of your battery?",
    "Could you share your battery percentage with me?",
    "What percentage of battery do you have?",
    "Can you provide details about your battery status?",
    "What's your battery level right now?",
    "How much charge is left in your battery?",
    "Could you reveal your battery percentage?",
    "What is your current power level?",
    "Can you inform me about your remaining battery?",
    "What is the level of your current battery charge?",
    "Could you disclose your battery level?",
    "How much power is left in your battery?",
    "What's the remaining percentage on your battery?",
    "Can you share your current battery status?",
    "What percentage of battery power are you currently at?",
    "Could you tell me your battery percentage?",
    "How is your battery doing right now?",
    "What's the percentage of charge left in your battery?",
    "Can you inform me about your battery percentage?",
    "What is the remaining power in your battery?",
    "Could you disclose your current battery level?",
    "What is your battery charge percentage?",
    "Can you share your current battery level?",
    "What's your battery status?",
    "Could you tell me the percentage of charge in your battery?",
    "What's your battery charge level?",
    "Can you disclose your current battery status?",
    "What is the current level of your battery charge?",
    "How much power do you have left?",
    "What's the battery percentage on your device?",
    "Could you inform me about your battery charge?",
    "What's your remaining battery charge percentage?",
    "Can you reveal your current battery charge?",
    "How much battery life do you have left?",
    "What is the charge percentage on your battery?",
    "Could you share your battery charge level?",
    "What is your battery power at the moment?",
    "Can you provide details about your battery charge?",
    "What's the percentage of power remaining in your battery?",
    "Could you inform me about your battery charge level?",
    "What is your current battery charge percentage?",
    "Can you disclose your remaining battery charge?",
    "How much battery capacity do you have left?",
    "What's your battery charge right now?",
    "Could you share your current battery status?",
    "What is the charge level on your battery?",
    "Can you inform me about your battery charge percentage?",
    "What's the remaining charge on your battery?",
    "Could you reveal your current battery charge level?",
    "How is your battery performing?",
    "What is your remaining battery charge percentage?",
    "Can you provide details about your remaining battery charge?",
    "What's your battery life percentage?",
    "Could you tell me your current battery charge level?",
    "What is your battery charge at the moment?",
    "Can you disclose your remaining battery power?",
    "How much charge is left in your battery right now?",
    "What's the percentage of battery remaining on your device?",
    "Could you inform me about your current battery charge?",
    "What is your current battery life percentage?",
    "Can you share your remaining battery charge level?",
    "What's the charge percentage left in your battery?",
    "Could you disclose your battery life percentage?",
    "How much battery power do you have left?",
    "What is your current battery power percentage?",
    "Can you reveal your battery life percentage?",
    "What's the remaining power percentage on your battery?",
    "Could you inform me about your battery power percentage?",
    "What is your current battery health percentage?",
    "Can you disclose your battery health percentage?",
    "What's the remaining health percentage of your battery?",
    "Could you share your battery health percentage?",
    "How much health is left in your battery?",
    "What is the health percentage of your battery?",
    "Can you provide details about your battery health percentage?",
    "What's the remaining battery health percentage?",
    "Could you inform me about your remaining battery health?",
    "How is your battery health percentage?",
    "What is your remaining battery health at the moment?",
    "Can you disclose your current battery health percentage?",
    "What is your battery health right now?",
]




# Output file path
output_file_path = 'dataset_battery.json'

# Transform the list of questions to JSON and save to file
transform_to_json(questions, output_file_path)
