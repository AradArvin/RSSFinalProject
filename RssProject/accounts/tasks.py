from celery import shared_task
from django.core.mail import send_mail


@shared_task()
def send_feedback_email_task(email_address, message):
    """Sends an email when the feedback form has been submitted."""
    send_mail(
        "Your Change Password link is: ",
        f"\t{message}\n\nThis link will be valid for 10 minutes.",
        "support@gmail.com",
        [email_address],
        fail_silently=False,
    )
