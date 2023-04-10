from func import code_p1, matrix, who_win

print('Это игра "Крестики-нолики". Вот игровое поле:')
for row in matrix:
    print("{:3} {:3} {:3}".format(*row))

code_p1()
if not who_win("  Х") and not who_win("  0"):
    print("Ничья!")
print("Спасибо за игру!")
