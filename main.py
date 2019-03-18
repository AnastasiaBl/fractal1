import ru_local

from turtle import *


def choice():
    print(ru_local.START)
    print(ru_local.EXAMPLE)
    print(ru_local.KOCH1)
    print(ru_local.KOCH2)
    print(ru_local.MINKOVSKI)
    print(ru_local.LEVI)
    print(ru_local.LED1)
    print(ru_local.LED2)
    print(ru_local.BRANCH)
    print(ru_local.TREE)
    print(ru_local.SNOWFLAKE1)
    print(ru_local.SNOWFLAKE2)
    print(ru_local.DRAGON)
    print()
    print('_' * 80)
    digits = int(input(ru_local.CHOICE))
    print('_' * 80)
    penup()
    goto(-200, 50)
    speed(10)
    pendown()
    if digits == 1:
        return example_of_rec()
    elif digits == 2:
        return main_koch()
    elif digits == 3:
        return snowflake_koch()
    elif digits == 4:
        return main_minkov()
    elif digits == 5:
        return main_levi()
    elif digits == 6:
        return main_led1()
    elif digits == 7:
        return main_led2()
    elif digits == 8:
        return main_branch()
    elif digits == 9:
        return main_tree()
    elif digits == 10:
        return snowflake1()
    elif digits == 11:
        return snowflake2()
    elif digits == 12:
        right(90)
        size = int(input(ru_local.SIZE))
        n = int(input(ru_local.N))
        return dragon_main(n, size)
    else:
        print(ru_local.END)




def ex(n, l):
    if n == 0:
        return
    right(10)
    forward(l // 10)
    pendown()
    for i in range(4):
        forward(l)
        right(90)
    penup()
    return ex(n - 1, int(0.9 * l))


def example_of_rec():
    n = int(input(ru_local.N))
    l = int(input(ru_local.SIZE))
    for i in range(4):
        forward(l)
        right(90)
    return ex(n, l)




def koch(order, size):
    if order == 0:
        forward(size)
    else:
        koch(order - 1, size / 3)
        left(60)
        koch(order - 1, size / 3)
        right(120)
        koch(order - 1, size / 3)
        left(60)
        koch(order - 1, size / 3)


def main_koch():
    order = int(input(ru_local.N))
    size = int(input(ru_local.SIZE))
    return koch(order, size)




def snowflake_koch():
    order = int(input(ru_local.N))
    size = int(input(ru_local.SIZE))
    for i in range(3):
        koch(order, size)
        right(120)




def minkov(n, size):
    if n == 0:
        forward(size)
        return
    else:
        minkov(n - 1, size)
        left(90)
        minkov(n - 1, size)
        right(90)
        minkov(n - 1, size)
        right(90)
        minkov(n - 1, size)
        minkov(n - 1, size)
        left(90)
        minkov(n - 1, size)
        left(90)
        minkov(n - 1, size)
        right(90)
        minkov(n - 1, size)


def main_minkov():
    n = int(input(ru_local.N))
    size = int(input(ru_local.SIZE))
    return minkov(n, size)




def levi(n, size):
    if n == 0:
        forward(size)
        return
    else:
        left(45)
        levi(n - 1, size)
        right(90 - 45 * (n - 1))
        levi(n - 1, size)


def main_levi():
    n = int(input(ru_local.N))
    size = int(input(ru_local.SIZE))
    return levi(n, size)




def led_1(n, size):
    if n == 0:
        forward(size)
        return
    else:
        led_1(n - 1, size)
        left(90)
        led_1(n - 1, size / 2)
        right(180)
        led_1(n - 1, size / 2)
        left(90)
        led_1(n - 1, size)


def main_led1():
    n = int(input(ru_local.N))
    size = int(input(ru_local.SIZE))
    led_1(n, size)




def led_2(n, size):
    if n == 0:
        forward(size)
        return
    else:
        led_2(n - 1, size * 2)
        left(120)
        led_2(n - 1, size)
        right(180)
        led_2(n - 1, size)
        left(120)
        led_2(n - 1, size)
        right(180)
        led_2(n - 1, size)
        left(120)
        led_2(n - 1, size * 2)


def main_led2():
    n = int(input(ru_local.N))
    size = int(input(ru_local.SIZE))
    led_2(n, size)





def branch(n, size):
    if n == 0:
        left(180)
        return

    x = size / (n + 1)
    for i in range(n):
        forward(x)
        left(45)
        branch(n - i - 1, 0.5 * x * (n - i - 1))
        left(90)
        branch(n - i - 1, 0.5 * x * (n - i - 1))
        right(135)

    forward(x)
    left(180)
    forward(size)


def main_branch():
    n = int(input(ru_local.N))
    size = int(input(ru_local.SIZE))
    left(90)
    branch(n, size)



def tree(n, size):
    if n == 0:
        forward(size)
    else:
        forward(size)
        right(30)
        tree(n - 1, size / 2)
        right(180)
        tree(n - 1, size / 2)
        right(120)
        tree(n - 1, size / 2)
        right(180)
        tree(n - 1, size / 2)
        right(30)
        forward(size)


def main_tree():
    n = int(input(ru_local.N))
    size = int(input(ru_local.SIZE))
    left(90)
    tree(n, size)




def snowflake1():
    n = int(input(ru_local.N))
    size = int(input(ru_local.SIZE))
    right(60)
    for _ in range(6):
        led_1(n, size)
        right(180)
        led_1(n, size)
        left(120)




def snowflake2():
    n = int(input(ru_local.N))
    size = int(input(ru_local.SIZE))
    right(60)
    for _ in range(6):
        led_2(n, size)
        right(180)
        led_2(n, size)
        left(120)




def dragon_main(n, size, lst=list()):
    forward(size)
    a = lst.copy()
    for i in range(len(a)):
        a[i] = not a[i]
    a.reverse()
    if n == 0:
        return
    lst = lst + [False] + a
    dragon([False] + a, size)
    return dragon_main(n - 1, size, lst)


def dragon(lst, size):
    for i in range(len(lst)):
        if lst[i]:
            right(90)
        else:
            left(90)
        if i != len(lst) - 1:
            forward(size)


def main():
    choice()
    done()


if __name__ == '__main__':
    main()




