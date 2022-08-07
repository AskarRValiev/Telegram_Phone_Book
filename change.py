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
    coinc = read_book.test_contact('phones.txt', data)
    if coinc != 'good':
        return coinc
    else:
        with open('phones.txt', 'a', encoding= 'utf-8') as file:
            file.write(data +'\n')
            return '1'
 

def delete_contact(name: str):
    
    with open('phones.txt', 'r', encoding='utf-8') as file:
        while True:
            line = file.read()
            print(line)
            if name in line:
                print('deact')
                file.close()
                return '1'
            else: 
                with open ('temp.txt', 'a', encoding='utf-8') as temp:
                    temp = temp.write(line)
                    print('not')
            if not line:
                break
            


delete_contact('Кондомский')

    






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



