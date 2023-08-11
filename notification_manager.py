import smtplib

# Use your own details.
EMAIL_DOMAIN = 'smtp.gmail.com'
SENDERS_EMAIL = 'test@gmail.com'
PASSWORD = 'xxxxxxxxxxxx'


class NotificationManager:
    """
    This class is responsible for sending notifications with the deal flight details.
    """

    def __init__(self, message_to_send):
        with smtplib.SMTP(EMAIL_DOMAIN) as connection:

            # Securing the Connection.
            connection.starttls()

            connection.login(user=SENDERS_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=SENDERS_EMAIL, to_addrs=SENDERS_EMAIL, msg=message_to_send)
