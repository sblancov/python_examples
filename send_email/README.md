# Send and email

First of all, I need to run an SMTP server, so I execute:

    make run-email-server

then, we can receive emails from our script executing:

    make run-script

Each time we run the script some lines are written by server to standard output:

    ---------- MESSAGE FOLLOWS ----------
    This is the cool message, it rocks.
    ------------ END MESSAGE ------------

# References

https://realpython.com/python-send-email/#option-2-setting-up-a-local-smtp-server
