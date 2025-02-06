import speech as sp
import random as r, time as t

# Niveles de dificultad
levels = {
    "easy": ["agenda", "ami", "souris"],
    "medium": ["ordinateur", "algorithme", "développeur"],
    "hard": ["réseau neuronal", "apprentissage automatique", "intelligence artificielle"]
}

def game(level):
    words = levels.get(level, [])
    if not words:
        print("This level doesn't exist")

        return

    score = 0
    attempts = 3

    for _ in range (len(words)):
        rword = r.choice(words)
        print(f"Pronounce the following word: {rword}")
        recog_word = sp.forGame()
        
        if rword == recog_word:
            cong = ["Right!", "Perfect!", "Good!"]
            print(r.choice(cong))
            print(f"You have spelt: {recog_word}")
            print("You get 1 point!")
            score += 1
        else:
            print(f"uh, oh. You spelt: {recog_word}.")
            print(f"The correct word was {rword}")
        t.sleep(3)
    print(f"Game over, your score is: {score}/{attempts}")
    return

level = input("Choose difficulty: (easy / medium / hard): ")

game(level)