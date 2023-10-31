import json
from difflib import get_close_matches

# Load the knowledge base from a JSON file
def load_knowledge_base(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        data: dict = json.load(file)
    return data

# Save the knowledge base to a JSON file
def save_knowledge_base(file_path: str, data: dict):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)

# Find the best match for user input in the list of questions
def find_best_match(user_question: str, questions: list) -> str | None:
    matches: list = get_close_matches(user_question, questions, n=1, cutoff=0.6)
    return matches[0] if matches else None

# Get the answer for a specific question from the knowledge base
def get_answer_for_question(question: str, knowledge_base: dict) -> str | None:
    for q in knowledge_base["questions"]:
        if q["question"] == question:
            return q["answer"]
    return None

def chat_bot():
    knowledge_base: dict = load_knowledge_base('knowledge_base.json')
    
    while True:
        user_input: str = input('You: ')
        
        if user_input.lower() == 'quit':
            break
        
        best_match: str | None = find_best_match(user_input, [q["question"] for q in knowledge_base["questions"]])
        
        if best_match:
            answer: str = get_answer_for_question(best_match, knowledge_base)
            print(f'Bot: {answer}')
        else:
            print('Bot: I don\'t know the answer. Can you teach me?')
            new_answer: str = input('Type the answer or "skip" to skip: ')
            
            if new_answer.lower() != 'skip':
                knowledge_base["questions"].append({"question": user_input, "answer": new_answer})
                save_knowledge_base('knowledge_base.json', knowledge_base)
                print('Bot: Thank you! I learned a new response!')


# construct used to check whether the Python script is being run directly by the Python interpreter, rather than being imported as a module into another script. This means that the chat_bot() function will only be executed if the Python script is run directly, not if it is imported into another script. It's a way to define the entry point of your script, ensuring that the chatbot logic is executed when the script is run as a standalone program.
if __name__ == '__main__':
    chat_bot()
