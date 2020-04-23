
rus = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new = []

with open("text4.txt", 'r') as f_obj:
    for i in f_obj:
        i = i.split(' - ', 1)
        new.append(rus[i[0]] + ' ' + i[1])
    print(new)

with open('text4.1.txt', 'w') as f_obj_2:
    f_obj_2.writelines(new)
