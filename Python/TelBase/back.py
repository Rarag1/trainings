import base
import front


def start():
    f_name, f_type = front.importing()
    action = front.actions()
    if action in ['wright', 'find', 'delete', 'export']:
        if action == 'wright':
            d_wright = front.wright()
            base.wright_data(f_name, f_type, d_wright)
        elif action == 'find':
            d_find1, d_find2 = front.find()
            base.read_file(f_name, f_type, d_find1, d_find2)
        elif action == 'delete':
            d_find1, d_find2 = front.find()
            result = base.read_file(f_name, f_type, d_find1, d_find2)
            d_delete = front.delete(result)
            if d_delete == 'y': base.drop(f_name, f_type, d_find1, d_find2)
        elif action == 'export':
            fn_old, ft_old, f_name, f_type = front.export()
            base.wright_file(fn_old, ft_old, f_name, f_type)
    else: start()


def restart():
    d_restart = front.ifrestart()
    if d_restart == "y": start()
    else: print("До новых встреч!")