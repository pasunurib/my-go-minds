import psutil
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def get_cpu_memory_utilization():
    cpu_percent = psutil.cpu_percent(interval=1)
    virtual_memory = psutil.virtual_memory()

    memory_utilization = {
        "total": virtual_memory.total,
        "available": virtual_memory.available,
        "used": virtual_memory.used,
        "percent": virtual_memory.percent
    }

    return cpu_percent, memory_utilization

def send_email(subject, message):
    from_email = "pasunuribhanu22@gmail.com"  # Your email address
    to_email = "prakashbanu362@gmail.com"  # Manager's email address
    password = "Bhanu@1997"  # Your email password

    msg = MIMEMultipart()
    msg["From"] = from_email
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.attach(MIMEText(message, "plain"))

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(from_email,password)
    server.sendmail(from_email, to_email, msg.as_string())
    server.quit()

def main():
    cpu_percent, memory_utilization = get_cpu_memory_utilization()

    subject = "Daily CPU and Memory Utilization Report"
    message = f"CPU Utilization: {cpu_percent:.2f}%\n"
    message += f"Memory Utilization:{memory_utilization}%\n"
    message += f"  Total Memory: {memory_utilization['total'] / (1024 ** 3):.2f} GB\n"
    message += f"  Used Memory: {memory_utilization['used'] / (1024 ** 3):.2f} GB\n"
    message += f"  Available Memory: {memory_utilization['available'] / (1024 ** 3):.2f} GB\n"
    message += f"  Memory Percent: {memory_utilization['percent']}%\n"

    send_email(subject, message)

if __name__ == "__main__":
    main()
