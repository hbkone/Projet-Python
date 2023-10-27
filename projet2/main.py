# main.py

from securite import Securite
from mdp import MDP
from passphrase import Passphrase

def main():

# Demande des critères à l'utilisateur
    print("Bonjour, veuillez entrer vos critères pour le mot de passe")
    length = int(input("Longueur du mot de passe : "))
    num_lowercase = int(input("Nombre de minuscules : "))
    num_uppercase = int(input("Nombre de majuscules : "))
    num_digits = int(input("Nombre de chiffres : "))
    num_special_chars = int(input("Nombre de caractères spéciaux : "))

    # Génération du mot de passe
    password_gen = MDP()
    generated_password, entropy, strength = password_gen.generate_password(length, num_lowercase, num_uppercase, num_digits, num_special_chars)

    # Affichage du mot de passe, de l'entropie et de la force
    print(f"Mot de passe généré : {generated_password}")
    print(f"Entropie : {entropy}")
    print(f"Force du mot de passe : {strength}")

    # Génération de passphrase

    # Liste des mots de la méthode de dés de l'EFF
    word_list = ["a", "ability", "abuse", "access", "accident", "account", "accuse", "achieve", "acid", "acoustic", "acquire", "address", "adjust", "admit", "adult", "advance", "advice", "aerobic", "affair", "afford", "African", "against", "agent", "air", "airport", "aisle", "alarm", "album", "alcohol", "alert", "alien", "all", "alley", "allow", "almost", "alone", "alpha", "already", "also", "alter", "always", "amateur", "amazing", "among", "amount", "amused", "analyst", "anchor", "ancient", "anger", "angle", "angry", "animal", "ankle", "announce", "annual", "another", "answer", "antenna", "antique", "anxiety", "any", "apart", "apology", "appoint", "approve", "april", "arch", "Arctic", "area", "argue", "arm", "armed", "armor", "army", "around", "arrange", "arrest", "arrive", "arrow", "art", "artefact", "artist", "ascend", "ash", "aside", "ask", "asleep", "aspect", "assault", "assert", "asset", "assign", "assist", "assume", "athlete", "atmosphere", "atom", "attack", "attend", "attract", "auction", "audit", "August", "aunt", "author", "auto", "autumn", "average", "avocado", "avoid", "awake", "aware", "away", "awesome", "awful", "awkward", "axis", "baby", "bachelor", "bacon", "badge", "bag", "balance", "balcony", "ball", "bamboo", "banana", "banner", "bar", "barely", "bargain", "barrel", "base", "basic", "basket", "battle", "beach", "bean", "beauty", "because", "become", "beef", "before", "begin", "behave", "behind", "believe", "below", "belt", "bench", "benefit", "best", "betray", "better", "between", "beyond", "bicycle", "bid", "bike", "bind", "biology", "bird", "birth", "bitter", "black", "blade", "blame", "blanket", "blast", "bleak", "blessing", "blind", "blood", "blossom", "blouse", "blue", "blur", "blush", "board", "boat", "body", "boil", "bomb", "bone", "bonus", "book", "boost", "border", "boring", "borrow", "boss", "bottom", "bounce", "box", "boy", "bracket", "brain", "brand", "brave", "bread", "breeze", "brick", "bridge", "brief", "bright", "bring", "brisk", "broccoli", "broken", "bronze", "broom", "brother", "brown", "brush", "bubble", "buddy", "budget", "buffalo", "build", "bulb", "bulk", "bullet", "bundle", "bunker", "burden", "burger", "burst", "bus", "business", "busy", "butter", "buy", "cabbage", "cabin", "cable", "cactus", "cage", "cake", "call", "calm", "camera", "camp", "can", "canal", "cancel", "candy", "cannon", "canoe", "canvas", "canyon", "capable", "capital", "captain", "car", "carbon", "card", "cargo", "carpet", "carry", "cart", "case", "cash", "casino", "castle", "casual", "cat", "catalog", "catch", "category", "cattle", "caught", "cause", "caution", "cave", "ceiling", "celery", "cement", "census", "ceremony", "certain", "chair", "chalk", "champion", "change", "chaos", "chapter", "charge", "chase", "chat", "cheap", "check", "cheese", "chef", "cherry", "chest", "chicken", "chief", "child", "chimney", "choice", "choose", "chronic", "chuckle", "chunk", "churn", "cigar", "cinnamon", "circle", "citizen", "city", "civil", "claim", "clap", "clarify", "claw", "clay", "clean", "clerk", "clever", "click", "client", "cliff", "climb", "clinic", "clip", "clock", "clog", "close", "cloth", "cloud", "clown", "club", "clump", "cluster", "clutch", "coach", "coast", "coconut", "code", "coffee", "coil", "coin", "collect", "color", "column", "combine", "come", "comfort", "comic", "common", "company", "concert", "conduct", "confirm", "congress", "connect", "consider", "control", "convince", "cook", "cool", "copper", "copy", "coral", "core", "corn", "correct", "cost", "cotton", "couch", "country", "couple", "course", "cousin", "cover", "coyote", "crack", "cradle", "craft", "cram", "crane", "crash", "crater", "crawl", "crazy", "cream", "credit", "creek", "crew", "cricket", "crime", "crisp", "critic",]
   
 # Demande à l'utilisateur de lancer les dés
    print("Lancez les dés comme décrit sur https://www.eff.org/fr/dice :")
    dice_rolls = []
    for i in range(5):
        # l'utilisateur entre deux chiffres séparés par une virgule
        while True:
            try:
                roll = input(f"Lancer {i + 1}: ").split(',')
                if len(roll) == 2:
                    dice_rolls.append((int(roll[0]), int(roll[1])))
                    break
                else:
                    print("Veuillez entrer deux chiffres séparés par une virgule.")
            except ValueError:
                print("Veuillez entrer des chiffres valides.")

    # Généreration de la passphrase en fonction des dés et affichage du résultat
    passphrase_gen = Passphrase()
    generated_passphrase = passphrase_gen.generate_passphrase(dice_rolls, word_list)
    print(f"Passphrase générée : {generated_passphrase}")

if __name__ == "__main__":
    main()
