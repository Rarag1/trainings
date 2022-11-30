def importing():
    f_name, f_type = input("Введите имя файла, расширение файла (txt/csv): ").split('.')
    return f_name, f_type


def actions():
    d_action = input("Выберите действие (wright, find, delete, export): ")
    return d_action


def wright():
    d_wright = input("Ведите фамилию, имя, телефон, коментарий: ")
    return d_wright


def find():
    d_find1, d_find2 = input("Ведите поле поиска: фамилия или имя или телефон или коментарий, введите значение поля: ").split('.')
    return d_find1, d_find2


def delete(result):
    d_delete = input("Вы хотите удалить этот контакт? (Y/N): ")
    return d_delete


def export():
    fn_old, ft_old = input("Введите имя старого файла, расширение старого файла (txt/csv): ").split('.')
    f_name, f_type = input("Введите имя нового файла, расширение нового файла (txt/csv): ").split('.')
    return fn_old, ft_old, f_name, f_type


def ifrestart():
    d_restart = input("Желаете что-то еще? (Y/N):")
    return d_restart