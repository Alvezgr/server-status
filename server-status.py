import requests.exceptions
import smtplib
import csv
from sending import _send_email
from handling_data import _open_data

def _get_server_status(data_open):
    try:
        r = requests.get(data_open[0][:-1], timeout=10)
        r.raise_for_status()  # Raises a HTTPError if the status is 4xx, 5xxx
    except (requests.exceptions.ConnectionError, requests.exceptions.Timeout):
        _send_email()

    except requests.exceptions.HTTPError:
        _send_email()

    else:
        print('all good!') #Drink mate peacefull

if __name__ == '__main__':
    _get_server_status(_open_data())
