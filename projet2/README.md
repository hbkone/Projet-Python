Ce programme Python permet de:
-Implémentez un testeur de mot de passe testant la force d’un mot de passe basé sur l’entropie
respectant les critères de l’ANSSI : https://www.ssi.gouv.fr/administration/precautions-
elementaires/calculer-la-force-dun-mot-de-passe/
-Implémentez un générateur de mot de passe aléatoire en fonction de critères que l’utilisateur
pourra sélectionner : nombre de minuscules, nombre de majuscules, nombre de chiffres,
nombre de caractères spéciaux. Affichez le mot de passe généré avec son entropie et sa force.
-Implémentez un générateur de passphrase en vous basant sur la méthode de dés de l’EFF :
https://www.eff.org/fr/dice.

## Instructions

 Exécutez le fichier `main.py`.
 Il sera demandé à l'utilisateur d'entrer ses critères
 Le programme génèrera un mot de passe
 Suivez les instructions pour lancer les dés comme décrit sur [EFF - Créer des passphrases](https://www.eff.org/fr/dice).
 Le programme générera une passphrase basée sur les résultats des dés.
 La passphrase générée sera affichée à l'écran.

## Structure des fichiers

- **main.py:** Fichier principal du programme.
- **passphrase.py:** Module contenant la classe `Passphrase` pour générer des passphrases.
- **securite.py** Module contenant la classe 'Securite' pour tester les mots de passe
- **mdp.py** Module contenant la classe MDP pour générer les mots de passe
- **README.md:** Ce fichier.

## Utilisation

Assurez-vous d'avoir Python installé sur votre système.
