# question.py
import random

class Question:
    def __init__(self, text, options, correct_option):
        self.text = text
        self.options = options
        self.correct_option = correct_option
        

    def shuffle_options(self):
        random.shuffle(self.options)

    def display_question(self):
        print(self.text)
        for i, option in enumerate(self.options, start=1):
            print(f"{chr(96 + i)}) {option}")

    def is_correct(self, user_choice):
        return user_choice.lower() == self.correct_option.lower()
