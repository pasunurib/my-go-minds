import psutil
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Function to get CPU utilization
def get_cpu_utilization():
    return psutil.cpu_percent(interval=1)

# Function to send an email report
def send_email(subject, body):
    # Email configuration
    sender_email = 'pasunuribhanu22@gmail.com'
    sender_password = 'Bhanu@1997'
    receiver_email = 'bpasunuri00@gmail.com'

    # Create message
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject

    # Attach the body of the email
    message.attach(MIMEText(body, 'plain'))

    try:
        # Establish a secure session with Gmail's outgoing SMTP server using your gmail account
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)

        # Send the email
        server.sendmail(sender_email, receiver_email, message.as_string())
        server.quit()
        print("Email sent successfully")
    except Exception as e:
        print(f"Error: {str(e)}")

# Get CPU utilization
cpu_utilization = get_cpu_utilization()

# Create and send the email report
subject = "CPU Utilization Report"
body = f"Current CPU Utilization: {cpu_utilization}%"
send_email(subject, body)
