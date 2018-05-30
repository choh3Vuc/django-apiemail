# django-apiemail
Email backend for django using some standard email API clients

django-apiemail is a Django email backend that conforms to the documented specification:

Email backends
The actual sending of an email is handled by the email backend.

The email backend class has the following methods:

open() instantiates a long-lived email-sending connection.
close() closes the current email-sending connection.
send_messages(email_messages) sends a list of EmailMessage objects. If the connection is not open, this call will implicitly open the connection, and close the connection afterwards. If the connection is already open, it will be left open after mail has been sent.
It can also be used as a context manager, which will automatically call open() and close() as needed:

It implements a context manager class with an open, close and send_mesages(email_messages) methods
