import numpy as np
import pandas as pd


def read_file(f_name, f_type, d_find1, d_find2):
    if d_find2.isdigit(): d_find2 = int(d_find2)
    if f_type == 'csv':
        data = pd.read_csv(f'{f_name}.{f_type}', delimiter=',')
    elif f_type == 'txt':
        data = pd.read_table(f'{f_name}.{f_type}', sep=',')
    result = data[data[d_find1] == d_find2]
    print(result)
    return result


def wright_data(f_name, f_type, d_wright):
    with open(f'{f_name}.{f_type}', 'a') as TB:
        TB.writelines(f'\n{d_wright}')
    return TB


def drop(f_name, f_type, d_find1, d_find2):
    if d_find2.isdigit(): d_find2 = int(d_find2)
    data = pd.read_table(f'{f_name}.{f_type}', sep=',')
    result = data[data[f'{d_find1}'] != d_find2]
    result.to_csv(f'{f_name}.{f_type}')
    print(result)
    return result


def wright_file(fn_old, ft_old, f_name, f_type):
    print(fn_old,'.',ft_old,'->', f_name,'.',f_type)
    with open(f'{fn_old}.{ft_old}', 'r') as tbold, open(f'{f_name}.{f_type}', 'w') as tbnew:
        for line in tbold:
            tbnew.write(line)
    return tbnew