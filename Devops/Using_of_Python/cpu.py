# Import psutil module for system information
import psutil

# Import smtplib module for email sending
import smtplib

# Define the CPU usage threshold in percentage
threshold = 20

# Define the sender and receiver email addresses
sender = "prakashbanu362@gmail.com"
receiver = "bpasunuri00@gmail.com"

# Define the email subject and body
subject = "CPU Usage Alert"
body = f"The CPU usage is above {threshold}%."

# Get the current CPU usage in percentage
cpu_usage = psutil.cpu_percent()

# Check if the CPU usage exceeds the threshold
if cpu_usage > threshold:
    # Create an SMTP object to connect to the email server
    smtp = smtplib.SMTP("localhost")
    # Format the email message with headers and body
    message = f"Subject: {subject}\n\n{body}"
    # Send the email message
    smtp.sendmail(sender, receiver,message)
    # Close the SMTP connection
    smtp.quit()
print(cpu_usage)
