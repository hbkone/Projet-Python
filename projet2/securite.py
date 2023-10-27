# securite.py

import math

class Securite:
    @staticmethod
    def calculate_entropy(password):
        unique_chars = set(password)
        entropy = math.log2(len(unique_chars)) * len(password)
        return entropy

    @staticmethod
    def test_password_strength(password):
        min_entropy = 56  # Valeur minimale d'entropie recommandée par l'ANSSI

        entropy = Securite.calculate_entropy(password)

        if entropy >= min_entropy:
            return "Mot de passe fort!"
        else:
            return "Mot de passe faible. Veuillez en choisir un plus fort."
