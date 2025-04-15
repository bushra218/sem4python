import smtplib, ssl

port = 587
smtp_server = "smtp.gmail.com"
sender_email = "kashishgupta@eng.rizvi.edu.in"
receiver_email = "sidrasolkar2005@gmail.com"
password = input("Type your password and press enter:")
message = """\
Subject: hello there

This is alien"""

context = ssl.create_default_context()
with smtplib.SMTP(smtp_server,port) as server:
    server.ehlo()
    server.starttls(context=context)
    server.ehlo()
    server.login(sender_email,password)
    server.sendmail(sender_email,receiver_email,message)
