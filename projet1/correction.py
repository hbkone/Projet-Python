# correction.py

import random
from question import Question  # Importe la classe Question du module question

class Correction:
    def __init__(self, questions,):
        self.questions = questions
        self.score = 0
        self.user_answers = []

    def add_question(self, question):
        self.questions.append(question)


    def shuffle_questions(self):
        random.shuffle(self.questions)
    #def shuffle_options(self):
     #   random.shuffle(self.options)

    def run_correction(self):
        for question in self.questions:
            print(question.text)
            for i, option in enumerate(question.options, start=1):
                print(f"{chr(96 + i)}) {option}")

            user_choice = input("Votre réponse (a, b, c): ")
            while user_choice.lower() not in ['a', 'b', 'c','A','B','C']:
                print("Veuillez choisir entre a, b et c.")
                user_choice = input("Votre réponse (a, b, c): ")
                question.user_choice = user_choice
                
            if question.is_correct(user_choice):
                     print("Bonne réponse!\n")
                     self.score += 1
            else:
                print(f"Mauvaise réponse. La réponse correcte était: {question.correct_option.upper()}.\n")

        print(f"Votre score final est: {self.score}/{len(self.questions)}")
#afficher la correction à la fin du quiz
    def show_correction(self):
        print("\n=== Corrigé ===")
        for question in self.questions:
            print(question.text)
            print(f"Réponse correcte : {question.correct_option.upper()}")
            print("------------------------")
            
        