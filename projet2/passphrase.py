
# passphrase.py

import random

class Passphrase:
    @staticmethod
    def generate_passphrase(dice_rolls, word_list):
        words = []

        for roll in dice_rolls:
            word_index = (roll[0] - 1) * 6 + roll[1] - 1
            words.append(word_list[word_index])

        passphrase = ' '.join(words)
        return passphrase

