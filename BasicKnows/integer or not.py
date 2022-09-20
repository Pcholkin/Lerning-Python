def pr_int(n2um):

    if n2um % 2 == 0:
        print(f'Число {n2um} четное')
    else:
        print(f'Число {n2um} не четное')

if __name__ == "__main__":                  # пробема была тут, в точке входа
    n2um=int(input("Введи число"))
    pr_int(n2um)

