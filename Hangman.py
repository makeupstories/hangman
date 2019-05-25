def hangman(word):
    wrong_times = 0
    stages = [
        "",
        " _________________         ",
        "|                |         ",
        "|                |         ",
        "|                |         ",
        "|                O         ",
        "|              / | \       ",
        "|               / \        ",
        "|                          ",
        "|__________________________",
    ]
    letters = list(word)
    board = ["__"] * len(word)
    win = False
    print("Welcome to Hangman!")

    while wrong_times < len(stages) - 1:
        print('\n')
        msg = "Guess a letter:"
        char = input(msg)
        if char in letters:
            cind = letters.index(char)
            board[cind] = char
            letters[cind] = '$'
        else:
            wrong_times += 1
        print((" ".join(board)))
        e = wrong_times + 1
        print("\n".join(stages[0:e]))
        if "__" not in board:
            print("You win!")
            print("".join(board))
            win = True
            break
    else:
        print('You failed!')

hangman("apple")