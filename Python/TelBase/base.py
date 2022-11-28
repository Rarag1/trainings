import numpy as np
import pandas as pd

# d_base = 'TelBase.csv'
# f_name = 'TelBase'
# f_type = 'csv'
# d_find1 = 'Lname'
# d_find2 = 'Tesla'


def read_file(f_name, f_type, d_find1, d_find2):
    data = pd.read_csv(f'{f_name}.{f_type}', delimiter=',')
    result = data[data[f'{d_find1}'] == d_find2]
    print(result)
    return result


def wright_data(f_name, f_type, d_wright):
    with open(f'{f_name}.{f_type}', 'a') as TB:
        TB.writelines(f'\n{d_wright}')
    return TB


# def drop(f_name, f_type, d_find1, d_find2):
#     data = pd.read_csv(f'{f_name}.{f_type}', delimiter=',')
#     result = data[data[f'{d_find1}'] == d_find2]
#     data.drop(result[0])


# def wright_file(f_name, f_type='csv'):
#     with open(f'{f_name}.{f_type}', 'a') as TB:
#         TB.writelines("\nBob, Bob, 55, friend")
#     return TB


# wright_file(f_name)
# print(read_file(f_name, f_type, d_find1, d_find2))
