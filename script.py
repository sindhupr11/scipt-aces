import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(sender_email, sender_password, receiver_email, subject, message):
    message_obj = MIMEMultipart()
    message_obj['From'] = sender_email
    message_obj['To'] = receiver_email
    message_obj['Subject'] = subject

    message_obj.attach(MIMEText(message, 'plain'))

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.set_debuglevel(1)
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(message_obj)
            print(f"Email sent successfully to {receiver_email}")

    except smtplib.SMTPAuthenticationError:
        print(f"Failed to authenticate with the SMTP server. Check your username/password.")
    except smtplib.SMTPConnectError:
        print(f"Failed to connect to the SMTP server. Check your network connection.")
    except smtplib.SMTPServerDisconnected:
        print(f"The SMTP server unexpectedly disconnected. Try again later.")
    except smtplib.SMTPRecipientsRefused:
        print(f"The recipient's email address was refused: {receiver_email}. Check the email address.")
    except smtplib.SMTPSenderRefused:
        print(f"The sender's email address was refused: {sender_email}. Check the email address.")
    except smtplib.SMTPDataError:
        print(f"The SMTP server refused to accept the message data.")
    except smtplib.SMTPException as e:
        print(f"An error occurred. Error: {str(e)}")
    except Exception as e:
        print(f"Failed to send email to {receiver_email}. Error: {str(e)}")
        print(f"SMTP Server Response: {e.smtp_error.decode()}")
        import traceback
        traceback.print_exc()

sender_email = 'emailid'
sender_password = 'password'  # Using application-specific password
subject = 'RSVP for CodeCrypt!'


participants = {

    'Sindhu P R':'sindhupr2003@gmail.com',
    'Anton Prince': 'antonprince95@gmail.com'
}
for name, email in participants.items():

    message = f'''Dear {name},

Congratulations! Your team has been selected to participate in the CodeCrypt Hackathon, and we are thrilled to have you on board.

To ensure a smooth and committed participation, we are implementing a security measure by collecting a caution fee of 800 rupees per team. This fee is a preventive measure to avoid cancellations after confirming your RSVP, which helps us allocate resources effectively.The entire amount will be refunded at the conclusion of the hackathon. We understand the financial commitment and assure you that this is solely a security measure to uphold the integrity of the event.
Please note that this RSVP is valid for 24 hours only. If we do not receive your response along with payment within this time frame, your RSVP won’t be considered and will be disqualified.

Fill the form here: https://airtable.com/appkcqVj1r454kClF/shrD9V4fztCb2vXKq

QR for payment:https://drive.google.com/file/d/17kWA05BxN77lPLkcUNP7HJcW3OSaO6qr/view?usp=drive_link

Refer to our rules and guidelines:https://bit.ly/codecryptguide

Whatsapp group link for further communications: https://chat.whatsapp.com/FocVstI9yGGGKi5XlXvSwv

We appreciate your understanding and cooperation in this matter. Your participation is invaluable to us, and we look forward to an exciting and successful CodeCrypt Hackathon together.
If you have any questions or concerns, feel free to reach out to our team at acescusat1@gmail.com 

Thank you and best regards,
Organizers,
CodeCrypt'''

    send_email(sender_email, sender_password, email, subject, message)


