a = input()
if a == '':
    print('ошибка: нет данных')
for i in a:
    d = a.count('o')
    D = a.count('O')
    e = a.count('x')
    E = a.count('X')
s = d + D
y = e + E
print(s)
print(y)
print(s == y)
