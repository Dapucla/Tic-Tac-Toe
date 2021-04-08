import sys

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]


def greeting():
    print("")
    print("------------------------")
    print("    Добро пожаловать    ")
    print("         в игру         ")
    print("     крестики-нолики    ")
    print("------------------------")
    print("      Правила игры:     ")
    print("    вводите значение    ")
    print("         X и Y          ")
    print("    для расположения    ")
    print("   элементов на доске   ")
    print("------------------------")
    print("")


greeting()
start_game = input("Введите Ok чтобы продолжить:")
start = start_game == "Ok"


def dashboard():
    print("\n")
    print("       " + board[0] + " | " + board[1] + " | " + board[2] + " ")
    print("       " + board[3] + " | " + board[4] + " | " + board[5] + " ")
    print("       " + board[6] + " | " + board[7] + " | " + board[8] + " ")
    print("\n")


dashboard()


def draw_check():
    count = 0
    for i in board:
        if i != "X" and i != "0":
            count += 1
    if count == 0:
        print("------------------------")
        print("---------НИЧЬЯ!---------")
        print("------------------------")
        sys.exit()


def position_elements_X():
    draw_check()
    coordinates = int(input("Введите координаты без пробелов(x>0,y>0 и <4): "))
    if coordinates == 11 and board[0] == "-":
        board[0] = "X"
    elif coordinates == 12 and board[1] == "-":
        board[1] = "X"
    elif coordinates == 13 and board[2] == "-":
        board[2] = "X"
    elif coordinates == 21 and board[3] == "-":
        board[3] = "X"
    elif coordinates == 22 and board[4] == "-":
        board[4] = "X"
    elif coordinates == 23 and board[5] == "-":
        board[5] = "X"
    elif coordinates == 31 and board[6] == "-":
        board[6] = "X"
    elif coordinates == 32 and board[7] == "-":
        board[7] = "X"
    elif coordinates == 33 and board[8] == "-":
        board[8] = "X"
    else:
        print("Эта ячейка уже занята или вы неверно ввели координаты")
        position_elements_0()

    if board[:3] == ["X", "X", "X"]:
        print("-----КРЕСТИКИ ПОБЕДИЛИ-----")
        dashboard()
    elif board[6:] == ["X", "X", "X"]:
        print("-----КРЕСТИКИ ПОБЕДИЛИ-----")
        dashboard()
    elif board[::3] == ["X", "X", "X"]:
        print("-----КРЕСТИКИ ПОБЕДИЛИ-----")
        dashboard()
    elif board[1::3] == ["X", "X", "X"]:
        print("-----КРЕСТИКИ ПОБЕДИЛИ-----")
        dashboard()
    elif board[::4] == ["X", "X", "X"]:
        print("-----КРЕСТИКИ ПОБЕДИЛИ-----")
        dashboard()
    elif board[2:7:2] == ["X", "X", "X"]:
        print("-----КРЕСТИКИ ПОБЕДИЛИ-----")
        dashboard()
    elif board[3:6] == ["X", "X", "X"]:
        print("-----КРЕСТИКИ ПОБЕДИЛИ-----")
        dashboard()
    elif board[2::3] == ["X", "X", "X"]:
        print("-----КРЕСТИКИ ПОБЕДИЛИ-----")
        dashboard()
    else:
        print("------------------------")
        print(" Ход переходит ноликам ")
        print("------------------------")
        dashboard()
        position_elements_0()


def position_elements_0():
    draw_check()
    coordinates = int(input("Введите координаты без пробелов(x>0,y>0 и x<4, y<4):"))
    if coordinates == 11 and board[0] == "-":
        board[0] = "0"
    elif coordinates == 12 and board[1] == "-":
        board[1] = "0"
    elif coordinates == 13 and board[2] == "-":
        board[2] = "0"
    elif coordinates == 21 and board[3] == "-":
        board[3] = "0"
    elif coordinates == 22 and board[4] == "-":
        board[4] = "0"
    elif coordinates == 23 and board[5] == "-":
        board[5] = "0"
    elif coordinates == 31 and board[6] == "-":
        board[6] = "0"
    elif coordinates == 32 and board[7] == "-":
        board[7] = "0"
    elif coordinates == 33 and board[8] == "-":
        board[8] = "0"
    else:
        print("Эта ячейка уже занята или вы неверно ввели координаты")
        position_elements_0()

    if board[:3] == ["0", "0", "0"]:
        print("-----НОЛИКИ ПОБЕДИЛИ-----")
        dashboard()
    elif board[6:] == ["0", "0", "0"]:
        print("-----НОЛИКИ ПОБЕДИЛИ-----")
        dashboard()
    elif board[::3] == ["0", "0", "0"]:
        print("-----НОЛИКИ ПОБЕДИЛИ-----")
        dashboard()
    elif board[1::3] == ["0", "0", "0"]:
        print("-----НОЛИКИ ПОБЕДИЛИ-----")
        dashboard()
    elif board[::4] == ["0", "0", "0"]:
        print("-----НОЛИКИ ПОБЕДИЛИ-----")
        dashboard()
    elif board[2:7:2] == ["0", "0", "0"]:
        print("-----НОЛИКИ ПОБЕДИЛИ-----")
        dashboard()
    elif board[3:6] == ["0", "0", "0"]:
        print("-----НОЛИКИ ПОБЕДИЛИ -----")
        dashboard()
    elif board[2::3] == ["0", "0", "0"]:
        print("-----НОЛИКИ ПОБЕДИЛИ-----")
        dashboard()
    else:
        print("------------------------")
        print("Ход переходит крестикам")
        print("------------------------")
        dashboard()
        position_elements_X()


position_elements_X()