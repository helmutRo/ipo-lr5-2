x1 = input("введите 1-ую строку: ") #ввод строки 1
x2 = input("введите 2-ую строку: ")#ввод строки 2
a = 0 #задается счетчик
for i in x1: # проверяет наличие x1
    if i in x2: #если есть во второй строке то засчитывает + 1 к счетчику
        a += 1 
print(("строки являются аниграмами " if a == len(x1) else "строки не являются аниграммами")) 
#выводит являются ли аниграммами через "если  счетчик равен строке 1"