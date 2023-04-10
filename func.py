
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = [7, 8, 9]

p1 = None
p2 = None


def find_element(p):
    for row in matrix:
        for element in row:
            if element == p:
                return element
                break
        else:
            continue
        break


def p_touch(p, point):
    if p in l1:
        elem = find_element(p)
        matrix[0][elem - 1] = point  #
        l1.remove(p)
        for row in matrix:
            print("{:3} {:3} {:3}".format(*row))
    elif p in l2:
        elem = find_element(p)
        matrix[1][elem - 4] = point
        l2.remove(p)
        for row in matrix:
            print("{:3} {:3} {:3}".format(*row))
    elif p in l3:
        elem = find_element(p)
        matrix[2][elem - 7] = point
        l3.remove(p)
        for row in matrix:
            print("{:3} {:3} {:3}".format(*row))
    else:
        print("Введите корректное значение")


def who_win(p):
    who = True
    if matrix[0][0] == p and matrix[1][0] == p and matrix[2][0] == p:
        return who
    elif matrix[0][1] == p and matrix[1][1] == p and matrix[2][1] == p:
        return who
    elif matrix[0][2] == p and matrix[1][2] == p and matrix[2][2] == p:
        return who
    elif matrix[0][0] == p and matrix[0][1] == p and matrix[0][2] == p:
        return who
    elif matrix[1][0] == p and matrix[1][1] == p and matrix[1][2] == p:
        return who
    elif matrix[2][0] == p and matrix[2][1] == p and matrix[2][2] == p:
        return who
    elif matrix[0][0] == p and matrix[1][1] == p and matrix[2][2] == p:
        return who
    elif matrix[0][2] == p and matrix[1][1] == p and matrix[2][0] == p:
        return who
    else:
        who = False
        return who


def code_p1():
    global p1
    global p2
    i = 0
    pl1 = True
    pl2 = True
    while i < 9:
        if pl1:
            try:
                p1 = int(input("Первый игрок, выберите цифру, на позицию которой хотите поставить Х: "))
                if p1 in l1 or p1 in l2 or p1 in l3:
                    p_touch(p1, "  Х")
                    pl2 = True
                    i += 1
                    who_win("  Х")
                    if who_win("  Х"):
                        i = 9
                        pl2 = False
                        print("Победил Первый игрок!")
                    if i == 9:
                        pl2 = False
                else:
                    print("Введите корректное значение")
                    pl2 = False
            except Exception:
                print("Введите корректное значение")
                pl2 = False
        if pl2:
            try:
                p2 = int(input("Второй игрок, выберите цифру, на позицию которой хотите поставить 0: "))
                if p2 in l1 or p2 in l2 or p2 in l3:
                    p_touch(p2, "  0")
                    i += 1
                    pl1 = True
                    who_win("  0")
                    if who_win("  0"):
                        i = 9
                        print("Победил Второй игрок!")
                else:
                    print("Введите корректное значение")
                    pl1 = False
            except Exception:
                print("Введите корректное значение")
                pl1 = False


