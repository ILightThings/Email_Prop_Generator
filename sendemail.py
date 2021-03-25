import smtplib
from email.message import EmailMessage
from csv import reader


def send_mail(to_email, subject, message, server_address='smtp.gmail.com',
              from_email='',username=''):
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email
    msg.add_header('Content-Type','text/html')
    msg.set_payload(message)
    
    print(msg)
    server = smtplib.SMTP_SSL(server_address, 465)
    server.set_debuglevel(1)
    server.login(username, 'emailpassword')  # Change Password Here
    server.send_message(msg)
    server.quit()
    print('successfully sent the mail.')


with open('emails.csv','r') as book:
    csv_reader = reader(book)
    for row in csv_reader:
        send_mail("recipent@email.com",subject=str(row[1]),message=str(row[2]).encode(),from_email=f'{row[0]} <exampleaccount@gmail.com>',username='exampleaccout@gmail.com') #Change Me




