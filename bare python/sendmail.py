import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email server's IP address and port
server_ip = 'xxx.xxx.xxx.xxx'  # Replace with the IP address of the email server
port = 25  # Replace with the appropriate port (e.g., 25 for SMTP)

# Sender and recipient email addresses
sender_email = 'your_email@example.com'  # Replace with your email address
recipient_email = 'recipient_email@example.com'  # Replace with the recipient's email address

# Email content
subject = 'Test Email from Python'
body = 'Hello,\nThis is a test email sent from Python.'

# Create a MIMEText object
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = recipient_email
msg['Subject'] = subject
msg.attach(MIMEText(body, 'plain'))

# Connect to the email server
with smtplib.SMTP(server_ip, port) as server:
    # Send the email
    server.sendmail(sender_email, recipient_email, msg.as_string())
    print('Email sent successfully')

