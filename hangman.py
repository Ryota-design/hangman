def hangman(word):
    wrong=0
    stages=["",
            "_________        ",
            "|       |        ",
            "|       |        ",
            "|       o        ",
            "|      /|~       ",
            "|      / >       ",
            "|                ",
            "|                "
            ]

    rletters=list(word)#rlettersはwordのリスト化⇒cat 'c' 'a' 't' 
    board=["_"]*len(word)#wordの長さの分だけ＿を用意してboardに入れる
    win=False
    print("Welcome to hangman!")
    while wrong<len(stages)-1:
        print("\n")
        msg="input one word"
        char = input(msg)#キーボード入力をcharへ入れる"
        if char in rletters:#もしキーボード入力値がrlettersの中にあれば、"
            cind=rletters.index(char)#rletterの中のcharと同じ文字がはいいているindexを取得する"
            board[cind]=char #キーボード入力でaが入れば、_a_"
            rletters[cind]='$' #rlettersの正解した文字を＄に変える⇒次回同じ文字をいれても飛ばされる"

        else:
            wrong += 1
            print(" ".join(board))
            e=wrong +1
            print("\n".join(stages[0:e]))
            if "_" not in board:
                print("You Win!")
                print(" ".join(board))
                win = True
                break

    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("You Lose! The answer is {}.".format(word))

import random

hangman(random.choice(['dog', 'cat', 'bird']))
