import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

context = ssl.create_default_context()

port = 465
smtp_server = "smtp.gmail.com"
sender_email = "example@example.com"  # Enter your address
password = "examplePassword"  # Enter your password


# function to send email
def send_email(receiver_email, subject, body):
    message = MIMEMultipart("alternative")
    message["Subject"] = subject 
    message["From"] = sender_email
    message["To"] = receiver_email
    message.attach(MIMEText(body, "plain"))
    try:
        server = smtplib.SMTP_SSL(smtp_server, port, context=context)
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        return True
    except:
        return False
    finally:
        server.quit()


send_email(receiver_email, subject, body)


# Use this link and enable for your gmail : https://www.google.com/settings/security/lesssecureapps


