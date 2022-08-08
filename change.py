import read_book

# ввод данных пользователем и запись в файл


# def add_contact():  
#     id = input('введите номер id')                    
#     name = input('Имя: ')
#     surname = input('Фамилия: ')
#     middlename = input ('Отчество: ')
#     phone = input('Номер телефона: ')
#     comment = input('Комментарий: ')
#     data = [id, name, surname, middlename, phone, comment]
#     write_data_one_string(data)
#     return [id, name, surname, middlename, phone, comment]

def write_data_one_string(data):
    '''
    Принимает строку с данными, проверяет на предмет совпадения ID, номера телефона с имеющимися в файле 
    и полнотой вводимых данных, если все в порядке - записывает в телефонную книгу и возвращает код '1',
    в противном случае возвращает код ошибки 
    '''
    coinc = read_book.test_contact('phones.txt', data)
    if coinc != 'good':
        return coinc
    else:
        with open('phones.txt', 'a', encoding= 'utf-8') as file:
            file.write(data +'\n')
            return '1'
 

def delete_contact(name: str):
    '''
    Принимает данные контакта, любая последовательность символов, возвращает все совпадения.
    '''
    with open('phones.txt', 'r', encoding='utf-8') as file:
        s = ''
        while True:
            ln = file.readline()
            if name in ln:   
                s += ln         #проверить, может зря удалил \n!!!
            if not ln:
                break
    return s
            
def delete_id(num: str):
    '''
    Принимает ID контакта который необходимо удалить, находит в исходном файле, создает временный фал, куда сохраняет
    не удаляемые контакты, после формирования не удаляемых файлов перезаписывает их в исходный файл.
    '''
    res = '-1'
    tmp = open('temp.txt', 'w', encoding='utf-8')
    tmp.close()

    with open('phones.txt', 'r', encoding='utf-8') as file:
        ln = file.readlines()
        for i, item in enumerate(ln):
            s = ln[i].split()
            if s[0] != num:
                with open('temp.txt', 'a', encoding='utf-8') as tmp:
                    tmp.write(' '.join(s) + '\n')       
            else: res = '1'

    with open('temp.txt', 'r', encoding='utf-8') as tmp:
        lns = tmp.readlines()
    with open('phones.txt', 'w', encoding='utf-8') as file:
        file.write(' '.join(lns))
    print(res)
    return res

                    

   
#delete_id('4')

    






# def write_data_dif_string(data):
#     with open('phones.txt', 'a') as file:
#         #for each in data:
#         file.write(data)
#         file.write('\n')
#             #file.write()



# def delete_contact():
#          self.loadAll()

#          entry_to_delete = input("Введите имя контакта: ")
#          if entry_to_delete in self.phonebook.keys():
#              del self.phonebook[entry_to_delete]
#              file = open(self.phones.txt, 'w')
#              for name, number in self.phonebook.items():
#                  string = name + '\t' + number + '\n'
#                  file.write(string)
#              file.close()
#              print("Контакт удален успешно")
#          else:
#              print("Контакт не найден")



