from django.core.mail.backends.base import BaseEmailBackend

import sendgrid-python
from sendgrid.helpers.mail import *


class sendgrid(BaseEmailBackend):

    def __init__(self):
        # os.environ.get('SENDGRID_API_KEY')
        self.sg = sendgrid.SendG0ridAPIClient(apikey=self.apikey)

    def send_messages(self, email_messages):
        successes =  0
        for e in email_messages:
            from_email = Email("test@example.com")
            to_email = Email("test@example.com")
            subject = "Sending with SendGrid is Fun"
            content = Content("text/plain", "and easy to do anywhere, even with Python")
            mail = Mail(from_email, subject, to_email, content)
            response = sg.client.mail.send.post(request_body=mail.get())
            if response[]:
                successes += 1
        return successes

    def open(self):
        pass

    def close(self):
        pass

    def __enter_(self):
        self.open()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()



# Copyright 2018 Lean Systems Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
