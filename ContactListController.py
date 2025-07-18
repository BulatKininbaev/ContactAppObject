from ContaktList import ContactList

# инициализация контроллера
class Controller:
    def __init__(self,phone_name:str,path_name:str):
        self.phone_name=phone_name
        if phone_name.__len__()==0:
            self.phone_name='NoName_Phone'
        self.path_name=path_name
        if path_name.__len__()==0:
            self.path_name='ContaktList.csv'
        self.contact_list=ContactList(self.phone_name,self.path_name)

    @staticmethod
    def print_menu():
        print('Выберете пункт меню от 0 до 6:')
        print(
            f'0 - Печать меню\n1 - Вывести список\n2 - Добавить контакт\n3 - Изменить контакт\n4 - Удалить контакт\n5 - Найти контакт\n6 - Выйтий и сохранить изменения')

    def show_contact_list(self):
        print(self.contact_list)

    def add_contact_list(self):
        value = input('Введите через запятую ФИО и Телефон и примечания (Пример - Петров,89845687124,Друг)')
        self.contact_list.add_contact(value)

    def change_contact_list(self):
        value = input('Введите через запятую ID ФИО и Телефон и примечания (Пример -22,Петров,89845687124,Друг)')
        self.contact_list.change_contact(value)

    def find_contact_list(self):
        value = input('Введите ФИО для поиска')
        self.contact_list.find_contact(value)

    def delete_contact_list(self):
        value = input('Введите ID контакта')
        self.contact_list.delete_contact(value)

    def exit_contact_list(self):
        self.contact_list.close_save_contactlist()
