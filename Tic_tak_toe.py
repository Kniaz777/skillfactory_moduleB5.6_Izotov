field =  [["-", "-", "-"],
          ["-", "-", "-"],
          ["-", "-", "-"]]

def draw_field():
    for x in field:
        print(x[0], x[1], x[2])


def cross():
    print("Ходит крестик X")
    string = int(input("Введите номер строки: "))
    column = int(input("Введите номер столбца: "))

    while string < 1 or string > 3 or column < 1 or column > 3 or field[string - 1][column - 1] == 'x' \
            or field[string - 1][column - 1] == 'o' or string.isdigit() == False:
        string = int(input("Введите номер строки заново: "))
        column = int(input("Введите номер столбца заново: "))

    field[string - 1][column - 1] = "x"

def zero():
    print("Ходит нолик 0")
    string = int(input("Введите номер строки: "))
    column = int(input("Введите номер столбца: "))

    while string < 1 or string > 3 or column < 1 or column > 3 or field[string - 1][column - 1] == 'x' \
            or field[string - 1][column - 1] == 'o':
        string = int(input("Введите номер строки заново: "))
        column = int(input("Введите номер столбца заново: "))

    field[string - 1][column - 1] = "o"

def chec():
    for x in field:
        if x[0] == x[1] == x[2] != "-":
            print("Победитель - ", x[0])
            victory[0] = 1
            break
    for i in range(0, 2):
        if field[0][i] == field[1][i] == field[2][i] != "-":
            print("Победитель - ", field[0][i])
            victory[0] = 1
            break
    if field[0][0] == field[1][1] == field[2][2] != "-":
        print("Победитель - ", field[0][0])
        victory[0] = 1

    elif field[0][2] == field[1][1] == field[2][0] != "-":
        print("Победитель - ", field[0][2])
        victory[0] = 1

print("Крестики-нолики 3 х 3.")

print("Это игровое поле:")
draw_field()
k = 0
victory = [0]

while True:
    cross()
    k += 1
    draw_field()
    chec()
    if victory[0] == 1:
        break
    elif k == 9:
        print("Ничья")
        break
    zero()
    chec()
    if victory[0] == 1:
        break
    k += 1
    draw_field()




