
def my_func():
    try:
        with open('text5.txt', 'w+') as f_obj:
            line = input('Введите цифры через пробел \n')
            f_obj.writelines(line)
            my_number = line.split()
        print(sum(map(int, my_number)))
    except IOError:
        print('Ошибка в файле')
    except ValueError:
        print('Неправильно набран номер. Ошибка ввода-вывода')


my_func()