# Можно ли от шоколадки размером n x m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками

n = int(input('Введите первое число n '))
m = int(input('Введите второе число m '))
k = int(input('Введите число долек '))

# print(k/n)
# print(int(k/n))
# print(k/m)
# print(int(k/m))
if k/n==int(k/n) or k/m==int(k/m):
    print("Можно")
else:
    print('Нельзя')