import smtplib
import ssl

print("""
██████╗░██╗░░░██╗███╗░░░███╗░█████╗░██╗██╗░░░░░
██╔══██╗╚██╗░██╔╝████╗░████║██╔══██╗██║██║░░░░░
██████╔╝░╚████╔╝░██╔████╔██║███████║██║██║░░░░░
██╔═══╝░░░╚██╔╝░░██║╚██╔╝██║██╔══██║██║██║░░░░░
██║░░░░░░░░██║░░░██║░╚═╝░██║██║░░██║██║███████╗
╚═╝░░░░░░░░╚═╝░░░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝╚══════╝
    """)

port = 465
context = ssl.create_default_context()
email = input("Enter Email: ")
password = input("Enter Password: ")
receivers = input("Enter Recivers: ")
message = input("Enter Message: ")
with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login(email, password)
    server.sendmail(email, receivers, message)
    print("Email Sent")
    input()
