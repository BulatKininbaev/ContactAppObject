import csv
import re

# модуль класса самого справочника
class ContactListError (Exception):
    pass

class ContactListPhone(ContactListError):
    def __init__(self,message:str):
        super().__init__(message)

class ContactListID(ContactListError):
    def __init__(self,message:str):
        super().__init__(message)


# класс для работы в кеше - основные методы.
class SimpleContactList:
    # последний ID
    new_id = 0

    # все равно из какого экземпляра счетчик один
    @classmethod
    def gen_new_id(cls) -> int:
        cls.new_id+=1
        return cls.new_id

    # проверка номера и без создания экземпляра
    @staticmethod
    def check_phone_number(phone_number)->bool:
        return not re.match(r'8\d{10}', phone_number) is None

    # инициализируем пустой справочник входящий параметр имя телефона
    def __init__(self,person_name:str):
        self.person_name=person_name
        self.contact_lst = {}

# dander метод печати списка через print
    def __str__(self):
        result=''
        if len(self.contact_lst)==0:
            result='Пустой список контактов'
        for key in self.contact_lst.keys():
            result+=f'Контакт ID - {key} [Фамилия - {self.contact_lst[key][0]}  Телефон - {self.contact_lst[key][1]} Описание - {self.contact_lst[key][2]}] \n'
        return  result

# добавление контакта
    def add_contact(self,contact_str: str) -> int:
        result=-1
        contact_ls=contact_str.split(',')
        try:
            if not SimpleContactList.check_phone_number(contact_ls[1]):
                raise ContactListPhone('Не верный формат номера телефона ')
            result = SimpleContactList.gen_new_id()
            self.contact_lst[str(result)] = contact_ls
            return result
        except ContactListPhone as e:
            print(e)
            return result

        # добавление контакта без блока try для проверки
    def add_contact_without_try(self, contact_str: str) -> int:
        result = -1
        contact_ls = contact_str.split(',')
        if not SimpleContactList.check_phone_number(contact_ls[1]):
            raise ContactListPhone('Не верный формат номера телефона ')
        result = SimpleContactList.gen_new_id()
        self.contact_lst[str(result)] = contact_ls
        return result



    # изменение контакта (что не передали то не меняем)
    def change_contact(self,contact_str: str)->int:
        result=-1
        contact_ls=contact_str.split(',')
        try:
            if not contact_ls[0] in self.contact_lst:
                raise ContactListID('Отсутствует такой ID контакта')
            if not SimpleContactList.check_phone_number(contact_ls[2]) and str(contact_ls[1]).__len__()>0 :
                raise ContactListPhone('Не верный формат номера телефона ')
            if str(contact_ls[1]).__len__()>0:
                self.contact_lst[contact_ls[0]][0] = contact_ls[1]
            if str(contact_ls[2]).__len__()>0:
                self.contact_lst[contact_ls[0]][1] = contact_ls[2]
            if str(contact_ls[3]).__len__()>0:
                self.contact_lst[contact_ls[0]][2] = contact_ls[3]
            result = int(contact_str[0])
            return result
        except ContactListID as e:
            print(e)
            return result
        except ContactListPhone as e:
            print(e)
            return result

# удалить контакт
    def delete_contact(self,contact_id: str)-> int:
        result=-1
        try:
            if not contact_id.isdigit():
                raise ValueError('Не верный формат ID контакта')
            if not contact_id in self.contact_lst:
                raise ContactListID('Отсутствует такой ID контакта')
            result=self.contact_lst.pop(contact_id)
            return result
        except ContactListID as e:
            print(e)
            return result
        except ValueError as e:
            print(e)
            return result

# найти контакт
    def find_contact(self,contact_fio: str)->str:
        result=''
        for fio, phone, comment in self.contact_lst.values():
            if fio.find(contact_fio) > -1:
                result+=f'[Фамилия -{fio}  Телефон - {phone}  Описание - {comment}]\n'
        if result.__len__()==0:
            result='Контактов не найдено'
        return result

#список контактов с привязкой к файлу
class ContactList(SimpleContactList):

# инициализируем и открываем файл
    def __init__(self,person_name:str,path_name:str):
        super().__init__(person_name)
        self.path_name=path_name
        # Читаем файл контактов
        with open(self.path_name, 'r', encoding='utf-8') as DiskFile:
            reader = csv.DictReader(DiskFile, delimiter=';')
            for row in reader:
                self.contact_lst[row['ID']] = [row['FIO'], row['PHONE'], row['COMMENT']]
        SimpleContactList.new_id=max(map(lambda x: int(x), self.contact_lst.keys()))

# запись в файл и выход
    def close_save_contactlist(self):
        with open(self.path_name, 'w', encoding='utf-8', newline='') as CloseFile:
            data = [['ID', 'FIO', 'PHONE', 'COMMENT']]
            for key in self.contact_lst.keys():
                data.append([key, self.contact_lst[key][0], self.contact_lst[key][1], self.contact_lst[key][2]])
            writer = csv.writer(CloseFile, delimiter=';')
            writer.writerows(data)


