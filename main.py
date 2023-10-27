from correction import Correction
from question import Question

# Définit les questions
questions_data = [
    ("Combien y a-t-il de millimètres dans 5 centimètres?", ["0.5", "50", "500"], "a"),
    ("Qui est le président actuel des USA?", ["Jo Trump", "Donald Biden", "Jo Biden"], "c"),
    ("Dans quel continent se trouve la Norvège?", ["Europe", "Pacifique", "Amérique"], "a"),
    ("quel est l'os le plus long du corps humain?", ["Humérus", "Tibia", "Fémur"], "c"),
    ("Quelle est la ville nommée ville de l'amour?", ["Madrid", "Paris", "Bamako"], "b"),
    ("A qui appartient le théorème : AB+BC=AC", ["Pythagore", "Freud", "Einstein"], "a"),
    ("Quelle est la formule chimique de l'eau?", ["O2H", "HC2", "H2O"], "c"),
    ("Combien d'heures y a-t-il dans 3 jours?", ["24h", "48h", "72h"], "c"),
    ("Combien de siècles font 300ans ?", ["3", "2", "5"], "a"),
    ("Lequel de ces animaux est un bovin?", ["pigeon", "boeuf", "chat"], "b"),
]

# Crée des instances de Question
questions = [Question(text, options, correct_option) for text, options, correct_option in questions_data]
options = [Question(text, options, correct_option) for text, options, correct_option in questions_data]
# Initialise et exécute la correction
correction = Correction(questions)
correction.shuffle_questions()

correction.run_correction()
correction.show_correction() 


#correction = Correction(questions)
#correction.display_correction()

#quiz.display_correction()
#correction.display_correct_answers()
# Affiche le corrigé
#print("\n=== Corrigé ===")
#for i, (question, user_answer) in enumerate(zip(correction.questions, correction.user_answers), start=1):
 #   correct_answer = question.correct_option.upper()
  #  print(f"Question {i}: {question.text} - Votre réponse: {user_answer.upper()}, Correcte: {correct_answer}")
