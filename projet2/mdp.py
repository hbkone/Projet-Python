# mdp.py


import random
import string
import math

class MDP:
    @staticmethod
    def calculate_entropy(password):
        unique_chars = set(password)
        entropy = math.log2(len(unique_chars)) * len(password)
        return entropy

    @staticmethod
    def generate_password(length, num_lowercase, num_uppercase, num_digits, num_special_chars):
        lowercase_chars = string.ascii_lowercase
        uppercase_chars = string.ascii_uppercase
        digit_chars = string.digits
        special_chars = string.punctuation

        # Vérification que les critères ne dépassent pas la longueur du mot de passe
        total_chars = num_lowercase + num_uppercase + num_digits + num_special_chars
        if total_chars > length:
            raise ValueError("La somme des critères ne peut pas dépasser la longueur du mot de passe.")

        # Génération du mot de passe en fonction des critères
        password = (
            ''.join(random.choice(lowercase_chars) for _ in range(num_lowercase)) +
            ''.join(random.choice(uppercase_chars) for _ in range(num_uppercase)) +
            ''.join(random.choice(digit_chars) for _ in range(num_digits)) +
            ''.join(random.choice(special_chars) for _ in range(num_special_chars)) +
            ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(length - total_chars))
        )

        # Mélanger le mot de passe pour plus de sécurité
        shuffled_password = ''.join(random.sample(password, len(password)))

        # Calculer l'entropie et la force du mot de passe
        entropy = MDP.calculate_entropy(shuffled_password)
        strength = "Fort" if entropy >= 40 else "Faible"

        return shuffled_password, entropy, strength
