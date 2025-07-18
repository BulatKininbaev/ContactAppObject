

from ContaktList import SimpleContactList,ContactListPhone
import pytest
import random

@pytest.mark.parametrize(
            "phone_str,expected",
             [('656853232',False)
              ,('89245698724',True)
              ,('89678423561',True)
              ]
)

def test_check_phone_number(phone_str:str,expected:bool):
    """ тест с parametrize"""
    result = SimpleContactList.check_phone_number(phone_str)
    assert result == expected


@pytest.fixture
def func_parametrize():
    """Генерация номеров телефонов"""
    spec_simbols=['-','',]
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    random.shuffle(numbers)
    phone_number = '8'+ ''.join(numbers[0:5]) + ''.join(spec_simbols[random.randint(0, 1)]) + ''.join(numbers[6:11]) + ''.join(numbers[5])
    result=phone_number.isdigit()
    return [phone_number,result]



def test_check_phone_number_3(func_parametrize):
    """Тест через fixture пять раз прогоним генератор номеров тут false при проверке быть не может"""
    for _ in range(0,5):
        result = SimpleContactList.check_phone_number(func_parametrize[0])
        assert result == func_parametrize[1]


@pytest.mark.parametrize(
            "contact_str,expected",
             [('Симанов,656853232,Подрядчик',False)
              ,('Веселовский,89245698724,Коллега',True)
              ,('Дарья,89678423561,Сестра',True)
              ]
)

def test_add_contact(contact_str:str,expected:bool):
    """ тест с parametrize. Данная задача не позволяет придумывать здесь более сложные тесты"""
    cont_lst = SimpleContactList('IPhone')
    result = cont_lst.add_contact(contact_str)
    assert (result>-1) == expected


def test_add_contact_raise():
    """Поймать ошибку не верного номера телефона. Я разобрался. Если raise в функции помещен в try, то никакого исключения я в тесте не поймаю.
    Оставил все в изначально виде и добавил функцию add_contact_without_try
    """
    cont_lst = SimpleContactList('IPhone')
    with pytest.raises(ContactListPhone):
        cont_lst.add_contact_without_try('Перов С.А,79248759654,друг')

