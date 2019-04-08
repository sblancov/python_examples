import smtplib, ssl


def config_server():
    port = 1025
    host = 'localhost'
    server = smtplib.SMTP(host, port)
    return server


def send_email(server):
    sender_email = "just_me"
    receiver_email = "cool_receiver"
    message = "This is the cool message, it rocks."
    server.sendmail(sender_email, receiver_email, message)


def main():
    server = config_server()
    send_email(server)


if __name__ == "__main__":
    main()
