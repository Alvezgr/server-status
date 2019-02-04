import csv

def _open_data():
    data = '.client_data.csv'
    with open(data, mode='r') as file:
        data_open = [data_access for data_access in file]
    return data_open

