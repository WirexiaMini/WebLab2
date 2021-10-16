def check(x): #функция для первого задания
    if x<0:
        return "Задано отрицательное число"
    temp = x
    roll = 0
    while(temp > 0):
        dop = temp % 10
        roll = roll * 10 + dop
        temp = temp // 10
    return x == roll

def ret3list(list): #функция для второго задания
    ls2 = []
    ls3 = []
    ls5 = []
    for i in range(0,len(list)):
        if list[i]%2==0:
            ls2.append(list[i])
        if list[i]%3==0:
            ls3.append(list[i])
        if list[i]%5==0:
            ls5.append(list[i])
    print (ls2)
    print (ls3)
    print (ls5)

def revers(num): #функция для третьего задания
    rev_num = 0 #почти аналогично палиндрому
    if num>0:
        while (num>0):
            dop=num%10
            rev_num=rev_num*10+dop
            num = num // 10
        return rev_num
    else:
        while (num<0):
            dop= num % -10
            rev_num=rev_num*10+dop
            num=(num//10)+1
        return rev_num

def sqrt(num, n): #функция для четвертого задания
    if num<0:
        return "Отрицательное число"
    approx = num / n #начальное приближение
    while True:
        bet = ((n-1)*approx + num / approx**(n-1)) / n #итерация улучшения точности
        if abs(approx - bet) < 0.00001: #проверка соответствия точности
            return bet
        approx = bet

def sim(num): #функция для пятого задания
    if (num > 100000):
        return "Число больше 100000"
    for i in range(2,num-1):
        if (num % i == 0): #проверка деления 
            return "false"
    return "true"

n = int(input("Введите число:")) #число для первой и третей функ
print(check(n))

ls = [ ] #список для второй функ
for i in range(1,51):
    ls.append(i)
ret3list(ls)

print(revers(n)) 

num = int(input("Введите число, корень которого найти:")) #для четвертой функ
s = float(input("Введите нужную степень корня:")) #для четвертой функ
print (sqrt(num, s))

idle = int(input("Введите число от 0 до 100000:")) #для пятой функ
print(sim(idle))