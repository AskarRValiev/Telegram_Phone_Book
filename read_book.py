
#from guide_export import to_dictionary
from os import read


file_path = 'phones.txt'

def reader(file_path: str):
    '''
    Принимает путь к файлу телефонной книги, возвращает записи телефонной книги
    '''
    with open(file_path, 'r', encoding='utf-8') as file:
        data = file.read()
    return data



def test_contact(file_path: str, contact: str):
    '''
    Принимает путь к файлу телефонной книги и данные нового контакта, проверяет совпадения с ID, номером телефона и 
    полнотой данных, в случае совпадения или неполноты данных возвращает код ошибки, если все в порядке возвращает 'good'
    '''
    cont_temp = contact.split()
    with open(file_path, 'r', encoding='utf-8') as file:
        while True:
            try:
                line = file.readline()
                line_temp = line.split()
              
                if line_temp == []:
                    return 'good'
                elif cont_temp[0] == line_temp[0]:
                    return 'to_id'
                elif cont_temp[4] == line_temp[4]:
                    return 'to_number'
            except:
                return '-1'
            




