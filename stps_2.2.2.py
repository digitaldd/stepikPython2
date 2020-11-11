'''
Алиса владеет интересной информацией, которую хочет заполучить Боб.
Алиса умна, поэтому она хранит свою информацию в зашифрованном файле.
У Алисы плохая память, поэтому она хранит все свои пароли в открытом виде в текстовом файле.

Бобу удалось завладеть зашифрованным файлом с интересной информацией и файлом с паролями, но он не смог
понять какой из паролей ему нужен. Помогите ему решить эту проблему.

Алиса зашифровала свою информацию с помощью библиотеки simple-crypt.
Она представила информацию в виде строки, и затем записала в бинарный файл результат работы метода simplecrypt.encrypt.

Вам необходимо установить библиотеку simple-crypt, и с помощью метода simplecrypt.decrypt узнать, какой из паролей
служит ключом для расшифровки файла с интересной информацией.

Ответом для данной задачи служит расшифрованная интересная информация Алисы.

Файл с информацией
Файл с паролями

Примечание:
Для того, чтобы считать все данные из бинарного файла, можно использовать, например, следующий код:

with open("encrypted.bin", "rb") as inp:
    encrypted = inp.read()

'''
from simplecrypt import decrypt as dc, DecryptionException

with open('/Users/mk/Documents/temp/encrypted.bin', 'rb') as str0:  # open the file from Mac
    encrypted = str0.read()
str0.close()  # close the file
print(encrypted)

passwords = []
with open('/Users/mk/Documents/temp/passwords.txt', 'r') as str1:  # open the file from Mac
    for line in str1:
        passwords.extend(line.strip().split())  # reading all lines in string
str1.close()  # close the file

for i in range(len(passwords)):
    print(passwords[i])
    try:
        print(dc(passwords[i], encrypted), "Yes!!")
        break
    except (DecryptionException):
        print(i, "No")
        pass
