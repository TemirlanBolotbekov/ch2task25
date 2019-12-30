#Напишите функцию которая находит самою длинную слово в строке.
# a = (input("Word :"))
# print(len(a))

text = (input('Type to text :'))

listWords = text.split()

longword = 0

for i in range(1,len(listWords)):
    if len(listWords[longword]) < len(listWords[i]):
        longword = i

print("long word-",listWords[longword])

