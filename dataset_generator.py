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
    "What tasks can you perform?",
    "Tell me about your capabilities.",
    "What are your functions?",
    "What can you do for me?",
    "Can you provide a list of your features?",
    "How do you assist users?",
    "Describe your abilities.",
    "What kind of tasks are you designed for?",
    "Tell me about the things you can accomplish.",
    "What functionalities do you offer?",
    "What is your purpose?",
    "Give me an overview of your capabilities.",
    "What are your skills?",
    "What kind of assistance can you provide?",
    "Can you list your functionalities?",
    "How can you help me?",
    "Tell me what you're capable of doing.",
    "Describe the things you're good at.",
    "What are your main features?",
    "Can you perform specific tasks?",
    "What services do you offer?",
    "How can you be useful to me?",
    "Enumerate your functions.",
    "What kind of support do you provide?",
    "What do you excel at?",
    "List your practical applications.",
    "What are your strengths?",
    "What tasks are within your scope?",
    "Tell me about your operational abilities.",
    "What do you bring to the table?",
    "Describe your range of functions.",
    "What functionalities are available?",
    "What is in your toolkit?",
    "How do you function?",
    "Elaborate on your capabilities.",
    "What services are at your disposal?",
    "What tasks are you skilled at?",
    "Explain your areas of expertise.",
    "What practical uses do you have?",
    "What features make you unique?",
    "How can you assist me in daily life?",
    "List your practical skills.",
    "What kind of problems can you solve?",
    "Detail your operational scope.",
    "How do you contribute to users' needs?",
    "Describe how you can be helpful.",
    "What functionalities do users find valuable?",
    "What are your strong points?",
    "Can you enumerate your functions?",
    "How do you add value to users?",
    "What do you excel in doing?",
    "What are your primary functions?",
    "How can you simplify tasks for users?",
    "Tell me about your practical applications.",
    "What tasks do users typically use you for?",
    "What do you bring to the table in terms of utility?",
    "Describe how users benefit from your features.",
    "What kind of assistance do you provide to users?",
    "List the ways you can support users.",
    "What is your primary role?",
    "Tell me about the range of things you can accomplish.",
    "What functionalities do you prioritize?",
    "Can you perform specialized tasks?",
    "What kind of functionalities do you specialize in?",
    "Describe your utility in daily life.",
    "How do users typically engage with your capabilities?",
    "What services do users commonly seek from you?",
    "What do you offer to enhance users' experiences?",
    "List the ways in which you simplify tasks for users.",
    "Describe your role in assisting and supporting users.",
    "How can you contribute to users' daily routines?",
    "What are your most requested functions?",
    "How do users leverage your capabilities in their activities?",
    "What functionalities do users appreciate the most?",
    "What do you do to make users' lives easier?",
    "Tell me about the tasks you are proficient in handling.",
    "How do users utilize your functionalities in their routines?",
    "What are the primary functionalities users seek from you?",
    "What unique features do you bring to users?",
    "List the ways in which you enhance users' productivity.",
    "How do you adapt to users' needs through your functionalities?",
    "What functionalities do you consider your core strengths?",
    "Tell me about your most valuable capabilities.",
]


# Output file path
output_file_path = 'dataset_functionalities.json'

# Transform the list of questions to JSON and save to file
transform_to_json(questions, output_file_path)
