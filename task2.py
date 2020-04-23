
my_f = open("text2.txt", "r")
content = my_f.read()
print(f'В файле находится:', content)

content = content.split()
my_f = open("text2.txt", "r")
print(f'Количество строк:', {len(content)})

my_f = open("text2.txt", "r")
content = my_f.readlines()

for i in range(len(content)):
    print(f'Количество символов в строке = {len(content[i])}')

my_f = open("text2.txt", "r")
content = my_f.read()
content = content.split(' ')
print(f'Общее количество слов - {len(content)}')
my_f.close()