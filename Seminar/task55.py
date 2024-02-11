'''Задача №55.
Задача №55 Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
Программа должна выводить данные
Программа должна сохранять данные в текстовом файле
Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
Использование функций. Ваша программа не должна быть линейной'''

# 1. Создание файла: +++
# - открываем файл на дозапись - это режим a - +++

# 2. Добавление контакта: +++
# - запросить у пользователя данные контакта +++
# - открываем файл на дозапись - это режим a -+++
# - добавить новый контакт +++

# 3. Вывод данных на экран: +++
# - открываем файл на чтение - r - +++
# - считать файл +++
# - вывести на экран +++

# 4. Поиск контакта:
# - выбор варианта поиска
# - запросить данные для поиска
# - открыть файл на чтение
# - считываем данные (контакты), сохраняем в переменную
# - осуществляем поиск контакта
# - выводим на экран найденный контакт

# 5. Создание UI: +++
# - вывести меню на экран - +++
# - запросить у пользователя вариант действия +++
# - запустить соответствующую функцию +++
# - осуществить возможность выхода из программы +++

def input_sername():
    return input('Введите фамилию контакта: ').title()

def input_name():
    return input('Введите имя контакта: ').title()

def input_patronymic():
    return input('Введите отчество контакта: ').title()

def input_phone():
    return input('Введите телефон контакта: ')

def input_address():
    return input('Введите адрес(город) контакта: ').title()

def create_contact():
    sername = input_sername()
    name = input_name()
    patronymic = input_patronymic()
    phone = input_phone()
    address = input_address()
    return f'{sername} {name} {patronymic}: {phone}\n{address}\n\n'


def add_contact():  
    with open("fonebook.txt", 'a', encoding='utf -8') as file:
        contact_str = create_contact()
        file.write(contact_str)


def create_list_contact():
    with open("fonebook.txt", 'r', encoding='utf -8') as file:
        contacts_str = file.read()
    return contacts_str.rstrip().split('\n\n')

def print_contacts():
    contacts_list = create_list_contact()
    for n, contact in enumerate(contacts_list, 1):
        print(n, contact)
    
def search_contact():
    print(
        'Возможные варианты поиска:\n'
        '1. По фамилии\n'
        '2. По мени\n'
        '3. По отчеству\n'
        '4. По телефону\n'
        '5. По адресу(город)'
        )

    var = input('Выберите вариант поиска: ')
    while var not in ('1', '2', '3', '4', '5'):
        print('Некорректный ввод!')
        var = input('Выберите вариант поиска: ')
    i_var = int(var) - 1

    search = input('Введите данные для поиска: ').title()
    with open("fonebook.txt", 'r', encoding='utf -8') as file:
        contacts_str = file.read()
    #print([contacts_str])
    contacts_list = contacts_str.rstrip().split('\n\n')
    #print(contacts_list)

    for str_contact in contacts_list:
        lst_contact = str_contact.replace(':', '').split()
        if search in lst_contact[i_var]:
            print(str_contact)


def copy_contact():
    contacts_list = create_list_contact()
    print_contacts()
    print()

    num_copy_contact = int(input('Введите номер строки для копирования контакта: '))
    print()

    with open("copy_fonebook.txt", 'a', encoding='utf -8') as file:
        file.write(contacts_list[num_copy_contact - 1])



def interface():
    with open("fonebook.txt", 'a', encoding='utf -8'):
        pass

var = 0
while var != '5':
    print()
    print(
        'Возможные варианты:\n'
        '1. Добавить контакт\n'
        '2. Вывести на экран\n'
        '3. Поиск контакта\n'
        '4. Копировать контакт\n'
        '5. Выход'
        )
    print()

    var = input('Выберите вариант действия: ')
    while var not in ('1', '2', '3', '4', '5'):
        print('Некорректный ввод!')
        var = input('Выберите вариант действия: ')
    print()

    match var:
        case '1':
            add_contact()  
        case '2':
            print_contacts()
        case '3':
            search_contact()
        case '4':
            copy_contact()
        case '5':
            print('До свидания!')


if __name__ == '_main_':
    interface()