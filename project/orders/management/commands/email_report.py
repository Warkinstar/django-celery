from datetime import timedelta, time, datetime
from django.core.mail import mail_admins
from django.core.management import BaseCommand
from django.utils import timezone
from django.utils.timezone import make_aware  # делает время с учетом зоны
from orders.models import Order


today = timezone.now()
tomorrow = today + timedelta(1)
# Совмещает время и день
today_start = make_aware(datetime.combine(today, time()))
today_end = make_aware(datetime.combine(tomorrow, time()))


class Command(BaseCommand):
    help = "Send Today's Orders Report to Admins"

    def handle(self, *args, **kwargs):
        orders = Order.objects.filter(confirmed_date__range=(today_start, today_end))

        if orders:
            message = ""

            for order in orders:
                message += f"{order} \n"

            subject = (
                f"Order Report for {today_start.strftime('%Y-%m-%d')} "
                f"to {today_end.strftime('%Y-%m-%d')}"
            )
            # Отправка админам из списка ADMINS
            mail_admins(subject=subject, message=message, html_message=None)

            self.stdout.write("E-mail Report was sent.")  # Сообщение в консоль
        else:
            self.stdout.write("No orders confirmed today.")
