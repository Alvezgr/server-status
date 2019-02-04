import smtplib
from handling_data import _open_data


#This function send the email to the receiver with the message that correspond
def _send_email():

    TO = _open_data()[3][:-1] #the receiver email like: example@example.com type str
    SUBJECT = 'Server Status' #the subject that you like
    TEXT = 'Hubo un Fallo en el servidor. Verificar' #the quote text in the email type str

    # Gmail Sign In
    gmail_sender = _open_data()[1][:-1]#the mail that are sending the messagge type: str
    gmail_passwd = _open_data()[2][:-1]#the password of the sender type str

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
    except Exception as e:
        print ('error sending mail', e)

    server.quit()

if __name__ == '__main__':
    _send_email()
