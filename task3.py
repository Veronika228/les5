with open('text3.txt', 'r') as my_file:
    rich = []
    poor = []
    my_list = my_file.read().split('\n')
    for i in my_list:
        i = i.split()
        if int(i[1]) < 20000:
            poor.append(i[0])
        rich.append(i[1])
print(f'Оклад меньше 20.000 {poor}, средний оклад {sum(map(int, rich)) / len(rich)}')