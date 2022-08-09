import read_book


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
            file.close()
            return '1'
 
#*********************************************************
def delete_contact(name: str):
    '''
    Принимает данные контакта, любая последовательность символов, возвращает все совпадения.
    '''
    with open('phones.txt', 'r', encoding='utf-8') as file:
        s = ''
        while True:
            ln = file.readline()
            if name in ln:   
                s += ln
            if not ln:
                break
    return s

#**********************************************
def delete_id(num: str):
    '''
    Принимает ID контакта который необходимо удалить, находит в исходном файле, создает временный файл, куда сохраняет
    не удаляемые контакты, после формирования файла перезаписывает его в исходный файл.
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
    return res
#********************************************************

def chng_id(name: str):
    '''
    Принимает ID контакта который необходимо изменить, находит в исходном файле, создает временный файл, куда сохраняет
    не изменяемые  и измененный контакты, после формирования файла перезаписывает его в исходный файл.
    '''
    res = '-1'
    tmp = open('temp.txt', 'w', encoding='utf-8')
    tmp.close()
    dt = name.split()
    print(dt)
    with open('phones.txt', 'r', encoding='utf-8') as file:
        ln = file.readlines()
        for i, item in enumerate(ln):
            s = ln[i].split()
            if s[0] != dt[0]:
                with open('temp.txt', 'a', encoding='utf-8') as tmp:
                    tmp.write(' '.join(s) + '\n') 
            else:
                if dt[1] == 'фамилия'.lower():
                    s[1] = dt[2]
                elif dt[1] == 'имя'.lower():      
                    s[2] = dt[2]
                elif dt[1] == 'отчество'.lower():      
                    s[3] = dt[2]
                else:   
                    s[4] = dt[2]
                with open('temp.txt', 'a', encoding='utf-8') as tmp:
                    tmp.write(' '.join(s) + '\n') 

    with open('temp.txt', 'r', encoding='utf-8') as tmp:
        lns = tmp.readlines()
    with open('phones.txt', 'w', encoding='utf-8') as file:
        file.write(' '.join(lns))
        file.close()
        res = '1'
    return res


#chng_id('3 фамилия Хорошев')





