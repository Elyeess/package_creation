from package_creation_tutorial.string_ops import reverse_string, count_vowels, capitalize_words

def main():
    """
    Main function to demonstrate the string operations.
    """
    test_string: str = "hello world"  # Chaîne d'exemple
    print("Hi! PARIS")


    # Affiche la chaîne d'origine
    print(f"Original string: {test_string}")
    # Affiche la chaîne inversée
    print(f"Reversed: {reverse_string(test_string)}")
    # Affiche le nombre de voyelles dans la chaîne
    print(f"Vowel count: {count_vowels(test_string)}")
    # Affiche la chaîne avec chaque mot capitalisé
    print(f"Capitalized: {capitalize_words(test_string)}")

if __name__ == "__main__":
    main()  # Exécute la fonction main lorsque ce fichier est exécuté directement
