from GeekBase.GBfront import *
import numpy as np
import pandas as pd

def wright1(file, d_wright):
    with open(f'{file}', 'a') as TB:
        TB.writelines(f'\n{d_wright}')
    return TB

def find1(file, find_field, find_value):
    if find_value.isdigit(): find_value = int(find_value)
    data = pd.read_table(f'{file}', sep=',')
    print(data)
    result = data[data[find_field] == find_value]
    print(result)
    return result

def delete1(file, find_field, find_value):
    if find_value.isdigit(): find_value = int(find_value)
    data = pd.read_table(f'{file}', sep=',')
    result = data[data[f'{find_field}'] != find_value]
    result.to_csv(f'{file}')
    print(result)
    return file


# def wright_file(fn_old, ft_old, f_name, f_type):
#     print(fn_old,'.',ft_old,'->', f_name,'.',f_type)
#     with open(f'{fn_old}.{ft_old}', 'r') as tbold, open(f'{f_name}.{f_type}', 'w') as tbnew:
#         for line in tbold:
#             tbnew.write(line)
#     return tbnew