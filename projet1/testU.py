import unittest
from question import Question
from correction import Correction

class TestCorrection(unittest.TestCase):
    
    questions_data = [
    ("Quel est le plus grand océan du monde?", ["Atlantique", "Pacifique", "Indien"], "b")
    ]
    questions = [Question(text, options, correct_option) for text, options, correct_option in questions_data]
    
    def test_run_correction(self):
        # Teste la méthode run_correction
        correction = Correction(self.questions)
        correction.run_correction() 

        self.assertEqual(correction.score, 0)

    def test_show_correction(self):
        # Teste la méthode show_correction
        correction = Correction(self.questions)
        correction.run_correction()

        try:
            correction.show_correction()
        except Exception as e:
            self.fail(f"show_correction a échoué avec l'erreur : {e}")

if __name__ == '__main__':
    unittest.main()
