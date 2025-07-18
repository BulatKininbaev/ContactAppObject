from ContactListController import Controller

# Я так понимаю можно в main запихать **args and **kwargs, но это надо уточнить
def main():
    controller_contact_list = Controller('IPhone10R','ContaktList.csv')
    p_number=-1

    Controller.print_menu()

    while p_number != '6':
        p_number = input('Укажите пункт меню?')

        match p_number:
            case '0':
                Controller.print_menu()
            case '1':
                controller_contact_list.show_contact_list()
            case '2':
                controller_contact_list.add_contact_list()
            case '3':
                controller_contact_list.change_contact_list()
            case '4':
                controller_contact_list.delete_contact_list()
            case '5':
                controller_contact_list.find_contact_list()
            case _:
                continue
    else:
        controller_contact_list.exit_contact_list()
        print('Контакты сохранены')



if __name__ == "__main__":
    main()