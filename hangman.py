import random

def hangman():
    answer = ["cat","dog","bird","bear"]
    n = random.randint(0,3)
    word = answer[n]
    wrong = 0
    stages = ["",
              "______       ",
              "|            ",
              "|      |     ",
              "|      o     ",
              "|     /|/    ",
              "|     / /    ",
              "|            "
              ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("welcome to hungman!")
    
    while wrong < len(stages) - 1:
        print("\n")
        msg = "please expect a word"
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("you win")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("you lose collect is {}.".format(word))

hangman()

