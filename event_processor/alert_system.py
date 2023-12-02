import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


# Funktion zum Senden einer E-Mail-Benachrichtigung
def send_email_alert(
    subject,
    message,
    to_address,
    from_address,
    smtp_server,
    smtp_port,
    smtp_user,
    smtp_password,
):
    msg = MIMEMultipart()
    msg["From"] = from_address
    msg["To"] = to_address
    msg["Subject"] = subject

    body = MIMEText(message, "plain")
    msg.attach(body)

    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_user, smtp_password)
    text = msg.as_string()
    server.sendmail(from_address, to_address, text)
    server.quit()
