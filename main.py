import time
import random

def calculate_errors(original_text, user_input):
    original_words = original_text.split()
    user_words = user_input.split()
    
    errors = sum(1 for i in range(min(len(original_words), len(user_words))) if original_words[i] != user_words[i])
    errors += abs(len(original_words) - len(user_words))  # Account for missing or extra words
    
    return errors

def calculate_speed(start_time, end_time, user_input):
    elapsed_time = end_time - start_time
    words_per_minute = (len(user_input.split()) / elapsed_time) * 60
    return round(words_per_minute, 2)

def typing_speed_test():
    test_texts = [
        "Python is a powerful programming language.",
        "Practice makes perfect, so keep typing fast!",
        "Speed and accuracy are key in typing tests.",
        "He will get his money's worth in the long run.",
        "Success is not the key to happiness; happiness is the key to success."
    ]
    
    best_speed = 0
    
    while True:
        test_text = random.choice(test_texts)
        print("\nTyping Speed Test - Type the following text:\n")
        print(f"{test_text}\n")
        
        input("Press Enter when you are ready to start...")
        
        start_time = time.time()
        user_input = input("Start Typing: ")
        end_time = time.time()
        
        speed = calculate_speed(start_time, end_time, user_input)
        errors = calculate_errors(test_text, user_input)
        
        print("\nResults:")
        print(f"Typing Speed: {speed} WPM")
        print(f"Errors: {errors}")
        
        if speed > best_speed:
            best_speed = speed
        
        retry = input("\nDo you want to try again? (yes/no): ").strip().lower()
        if retry != "yes":
            print(f"\nYour Best Speed: {best_speed} WPM")
            print("Thanks for using the Typing Speed Test! Goodbye!")
            break

if __name__ == "__main__":
    typing_speed_test()
