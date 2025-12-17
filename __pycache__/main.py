import time
import random

# -------------------------------
# Typing Speed Test Sentences
# -------------------------------

sentences = [
    "Python is a powerful programming language.",
    "Typing fast requires regular practice.",
    "OpenAI helps build amazing applications.",
    "I love learning new technical skills.",
    "GitHub projects show your coding talent.",
    "Consistency is the key to success.",
    "Data science is the future of technology.",
    "Practice makes you faster at typing."
]

# -------------------------------
# Calculate Accuracy
# -------------------------------

def calculate_accuracy(original, typed):
    correct = 0
    min_length = min(len(original), len(typed))

    for i in range(min_length):
        if original[i] == typed[i]:
            correct += 1

    accuracy = (correct / len(original)) * 100
    return round(accuracy, 2)


# -------------------------------
# Count Words
# -------------------------------

def count_words(text):
    return len(text.split())


# -------------------------------
# Typing Test
# -------------------------------

def typing_test():

    print("\n========== TYPING SPEED TEST ==========")
    input("Press ENTER to start...")

    sentence = random.choice(sentences)

    print("\nType this sentence:\n")
    print(f"  {sentence}\n")

    start_time = time.time()

    user_input = input("Your typing ➜ ")

    end_time = time.time()

    total_time = round(end_time - start_time, 2)

    words = count_words(sentence)

    # WPM Calculation
    wpm = round((words / total_time) * 60)

    # Accuracy Calculation
    accuracy = calculate_accuracy(sentence, user_input)

    print("\n-------------- RESULT ----------------")
    print(f"Time Taken : {total_time} seconds")
    print(f"Words Typed: {words}")
    print(f"Speed (WPM): {wpm}")
    print(f"Accuracy   : {accuracy}%")
    print("--------------------------------------\n")


# -------------------------------
# Run App Loop
# -------------------------------

while True:
    typing_test()

    retry = input("Retry? (y/n): ")

    if retry.lower() != "y":
        print("\nThanks for using Typing Speed Test! 🙌")
        break
