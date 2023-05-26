

def show_data():
    with open('data.txt', 'r', encoding='utf-8') as file:
        book = file.read()
    return book


def new_data():
    with open('data.txt', 'a', encoding='utf-8') as file:
        file.write(input(' Введенные данные: '+'\n'))


def find_data():
    with open('data.txt', 'r', encoding='utf-8') as file:
        book = file.read().split('\n')
        temp = input()
        for i in book:
            if temp in i:
                print(i)

def change_data():
 
    book = open('data.txt', 'r', encoding='utf-8').read().split('\n')
    temp = input()
    new_data=input()
    for i in book:
        if temp in i:
          book[book.index(i)]=new_data     

    with open('data.txt', 'w', encoding='utf-8') as file2:
            file2.write('\n'.join(book))
        

def delete_data():
    book = open('data.txt', 'r', encoding='utf-8').read().split('\n')
    temp = input()
    for p in book:
        if temp in p:
            book.pop(book.index(p))  

    with open('data.txt', 'w', encoding='utf-8') as file2:
            file2.write('\n'.join(book))
                    
while True:
    mode = input('Выберите режим работы справочника:\
                 \n 1. Показать содержимое справочника\
                 \n 2. Добавление новой информации в справочник\
                 \n 3. Поиск в справочнике\
                 \n 4. Удаление данных в справочнике\
                 \n 5. Изменение данных в справочнике\
                 \n')
    if mode == '1': print(show_data())
    elif mode == '2':new_data()
    elif mode == '3':find_data()
    elif mode == '4':change_data()
    elif mode == '5':delete_data()
    else:print('No mode')
    break
