import smtplib, ssl


def main():
    port = 1025
    server = 'localhost'
    context = ssl.create_default_context()
    sender_email = "just_me"
    receiver_email = "cool_receiver"
    message = "This is the cool message, it rocks."
    email_server = smtplib.SMTP(server, port)
    email_server.sendmail(sender_email, receiver_email, message)


if __name__ == "__main__":
    main()
