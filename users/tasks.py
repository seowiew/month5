import time
from celery import shared_task
from django.core.mail import send_mail

@shared_task
def generate_report():
    print("generating a new report...")
    time.sleep(10)
    print("report generated!")

@shared_task
def clean_old_files():
    print("deleting old files...")
    time.sleep(5)
    print("old files deleted!")


@shared_task
def send_test_email_task(to_email):
    send_mail(
        subject='Тестовое письмо от Celery',
        message='Это тестовое письмо, отправленное через Celery с помощью SMTP.',
        from_email='geeksstudy25@gmail.com',  # email из настроек
        recipient_list=[to_email],
        fail_silently=False,
    )