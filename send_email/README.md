# Send and email

First of all, I need to run an SMTP server, so:

    python -m smtpd -n -c DebuggingServer localhost:1025

then, we can receive emails from our script.
