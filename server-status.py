import requests.exceptions
import smtplib
import csv

def _get_server_status():
    try:
        r = requests.get('host_server_name', timeout=10)
        r.raise_for_status()  # Raises a HTTPError if the status is 4xx, 5xxx
    except (requests.exceptions.ConnectionError, requests.exceptions.Timeout):
        return 0
    except requests.exceptions.HTTPError:
        return 2
    else:
        return 1 # Proceed to do snuff


def _send_email():
    data = '.client_data.csv'
    with open(data, mode='r') as file:
        all_data = [data_access for data_access in file]


if __name__ == '__main__':
    _send_email()
    response = _get_server_status()
    if response == 0:
        print('down')
    else:
        TO = ''
        SUBJECT = 'Server Status'
        TEXT = 'Parece que el servidor esta caido'

        # Gmail Sign In
        gmail_sender = ''
        gmail_passwd = ''

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_sender, gmail_passwd)

        BODY = '\r\n'.join(['To: %s' % TO,
                    'From: %s' % gmail_sender,
                    'Subject: %s' % SUBJECT,
                    '', TEXT])

        try:
            server.sendmail(gmail_sender, [TO], BODY)
            print ('email sent')
        except:
            print ('error sending mail')

        server.quit()
        print('good')
