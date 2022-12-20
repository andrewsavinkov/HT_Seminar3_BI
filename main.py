
# 1) Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint

def random_list(length):
    array = []
    for i in range(length):
        array.append(randint(0, 10))
    print(array)
    return array

def sum_of_uneven(input_list):
    sum = 0
    for i in range(1, len(input_list), 2):
        sum=sum+input_list[i]
    return sum

rnd=random_list(10)
print(sum_of_uneven(rnd))

# 2) Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

lst=[2, 3, 4, 5, 6, 7, 8]
# lst.__delitem__(len(lst)-1)
# print(lst)

def pair_mult(input_list):
    lst=[]
    if not len(input_list) % 2:
        for i in range(len(input_list)//2):
            lst.append(input_list[0]*input_list[len(input_list)-1])
            input_list.__delitem__(0)
            input_list.__delitem__(len(input_list)-1)
        print(lst)
    else:
        for i in range(len(input_list) // 2):
            lst.append(input_list[0] * input_list[len(input_list) - 1])
            input_list.__delitem__(0)
            input_list.__delitem__(len(input_list) - 1)
        lst.append(input_list[len(input_list) // 2]**2)
        print(lst)

pair_mult(lst)

# 3) Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов, отличной от 0.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

lst=[1.1, 1.2, 3.1, 5, 10.01]
def diff_of_float(input_list):
    new_lst=[]
    help_lst=[]
    diff=0
    for i in input_list:
        new_lst.append(str(i).split('.'))

    for i in range(len(input_list)):
        help_lst.append(round(input_list[i]%int(new_lst[i][0]), 2))
    while 0 in help_lst:
        help_lst.__delitem__(help_lst.index(0))

    print(f'{input_list} => {max(help_lst)-min(help_lst)}')
diff_of_float(lst)

# 4) Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

def dec_to_bin(input_num):
    num = '{0:08b}'.format(input_num)
    print(num)

n=2
dec_to_bin(n)

# 5) Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи

def fibo(n):
    if n>0:
        if n in (1, 2):
            return 1
        return fibo(n-1)+fibo(n-2)
    elif n<0:
        if n in (-1, -2):
            return -1
        return fibo(n+1)+fibo(n+2)
    else:
        return 0

def negafibo(input_num):
    lst=[]
    fibo_lst=[]
    for i in range(-input_num, input_num+1):
        lst.append(i)
    for i in lst:
        fibo_lst.append(fibo(i))
    print(f'{fibo_lst} Негафибоначчи')

n=8
negafibo(n)
