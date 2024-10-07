import smtplib
from email.mime.text import MIMEText
from getpass import getpass

# Prompt for user input
sender_email = input("Enter your Gmail address: ")
receiver_email = input("Enter the recipient email: ")
app_password = getpass("Enter your Gmail App Password (input hidden): ")
subject = "Test Email from Python Script"
body = "This is a test email sent from a Python script using Gmail's SMTP server and an App Password."

# Create the email message with MIMEText
message = MIMEText(body)
message['Subject'] = subject
message['From'] = sender_email
message['To'] = receiver_email

try:
    # Connect to Gmail's SMTP server using SSL
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(sender_email, app_password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        print("Email sent successfully!")
except Exception as e:
    print("Failed to send email:", e)
