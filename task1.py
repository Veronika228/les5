
my_f = open("text.txt", 'w')
my_words = input('Введите текст...\n')

while my_words:
    my_f.writelines(my_words)
    my_words = input('Введите текст...\n')
    if not my_words:
        break
my_f.close()

my_f = open("text.txt", "r")
content = my_f.readlines(my_words)
content = content.split(' ')
print(content)
my_f.close()
