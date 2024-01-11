import json

def transform_to_json(questions, output_file):
    json_data = []

    for index, question in enumerate(questions, start=1):
        json_entry = {
            "question": question,
            "answer": f"general_knowledge"
        }
        json_data.append(json_entry)

    with open(output_file, 'w') as file:
        json.dump(json_data, file, indent=2)

questions = [
    "What is the capital of Australia?",
    "Who wrote the play 'Romeo and Juliet'?",
    "In which year did World War II end?",
    "What is the largest mammal on Earth?",
    "Who painted the Mona Lisa?",
    "What is the currency of Japan?",
    "In which country is the Great Barrier Reef located?",
    "Who discovered penicillin?",
    "What is the boiling point of water in Celsius?",
    "Who is known as the 'Father of Modern Physics'?",
    "What is the process of photosynthesis?",
    "Who wrote 'To Kill a Mockingbird'?",
    "What is the longest river in the world?",
    "In which year did the Titanic sink?",
    "Who developed the theory of relativity?",
    "What is the chemical symbol for gold?",
    "Which planet is known as the Red Planet?",
    "What is the main component of Earth's atmosphere?",
    "Who was the first woman to win a Nobel Prize?",
    "In which year did the United States declare independence?",
    "What is the speed of light in a vacuum?",
    "Who painted the Starry Night?",
    "What is the largest ocean on Earth?",
    "In which country is Mount Everest located?",
    "Who wrote '1984'?",
    "What is the largest desert in the world?",
    "Who is the author of the Harry Potter series?",
    "What is the capital of Canada?",
    "In which year did the Berlin Wall fall?",
    "Who was the first man to step on the moon?",
    "What is the currency of Brazil?",
    "What is the meaning of the word 'ephemeral'?",
    "Who discovered electricity?",
    "What is the population of India?",
    "In which century did the Renaissance begin?",
    "Who painted the Sistine Chapel ceiling?",
    "What is the largest planet in our solar system?",
    "What is the capital of China?",
    "Who is known as the 'Bard of Avon'?",
    "What is the pH of pure water?",
    "In which country is the Taj Mahal located?",
    "Who wrote 'Pride and Prejudice'?",
    "What is the currency of South Africa?",
    "What is the speed of sound in air?",
    "Who developed the theory of evolution by natural selection?",
    "What is the smallest prime number?",
    "In which country is the Nile River located?",
    "Who composed the 'Moonlight Sonata'?",
    "What is the main ingredient in guacamole?",
    "What is the boiling point of water in Fahrenheit?",
    "Who painted the Last Supper?",
    "What is the capital of Russia?",
    "In which year did Christopher Columbus reach the Americas?",
    "Who discovered penicillin?",
    "What is the chemical symbol for oxygen?",
    "Who is the author of 'The Catcher in the Rye'?",
    "What is the capital of France?",
    "In which year did the American Civil War end?",
    "Who wrote 'War and Peace'?",
    "What is the largest species of big cat?",
    "What is the meaning of the word 'ubiquitous'?",
    "Who developed the theory of psychoanalysis?",
    "In which country is the Amazon Rainforest located?",
    "Who is known as the 'Queen of Pop'?",
    "What is the currency of Mexico?",
    "What is the capital of Italy?",
    "Who wrote 'The Odyssey'?",
    "What is the speed of a cheetah?",
    "In which year did the Industrial Revolution begin?",
    "Who discovered the polio vaccine?",
    "What is the main gas responsible for the greenhouse effect?",
    "Who is known as the 'Father of Medicine'?",
    "What is the largest moon of Saturn?",
    "In which year did the Cold War end?",
    "Who composed the 'Four Seasons'?",
    "What is the capital of South Korea?",
    "In which country is Machu Picchu located?",
    "Who wrote 'The Great Gatsby'?",
    "What is the currency of Japan?",
    "What is the boiling point of water at sea level?",
    "Who developed the theory of continental drift?",
    "What is the largest bird in the world?",
    "In which century was the first computer invented?",
    "Who painted the Guernica?",
    "What is the capital of Spain?",
    "Who wrote 'The Canterbury Tales'?",
    "What is the currency of Australia?",
    "What is the meaning of the word 'esoteric'?",
    "Who discovered the first antibiotic?",
    "What is the population of China?",
    "In which year did the Russian Revolution occur?",
    "Who is known as the 'King of Rock and Roll'?",
    "What is the currency of India?",
    "What is the main component of the Earth's core?",
    "Who wrote 'The Iliad'?",
    "What is the capital of Argentina?",
    "What is the boiling point of water in Kelvin?",
    "Who developed the theory of general relativity?",
    "In which country is the Serengeti National Park located?",
    "Who composed the 'Ode to Joy'?"
]


# Output file path
output_file_path = 'dataset_general_knowledge.json'

# Transform the list of questions to JSON and save to file
transform_to_json(questions, output_file_path)
