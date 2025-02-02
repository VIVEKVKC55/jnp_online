from django.utils import timezone
from django.core.signing import Signer
from django.conf import settings
from django.template.loader import get_template
from django.core.mail import send_mail

class SendResetPasswordMail:
    """Send Reset Password email to user."""

    def __init__(self, *agrs, **kwargs):
        self.email_data = kwargs.get("email_data", {})
        self.email = self.email_data.get("email")
        self.request = self.email_data.get("request")
        self.token = self.email_data.get("token")
        self.uid_b64 = self.email_data.get("uid_b64")

    def send(self):
        template_src = "default/mails/reset_password_link.html"
        template = get_template(template_src)

        subject = "Password Reset Requested"

        try:
            sent_to = self.email
            context = {
                "uid": self.uid_b64,
                "token": self.token,
            }
            body = template.render(context)


            send_mail(
                subject,
                body,
                settings.DEFAULT_FROM_EMAIL,
                [sent_to],
                fail_silently=False,
                html_message=body,
            )
        except Exception as e:
            print("Error: ", e)