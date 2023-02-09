from celery import shared_task
from django.core.mail import send_mail
from .models import Order

@shared_task
def order_created(order_id):
#     Task to send an e-mail notification when an order is
#     successfully created.
        order = Order.objects.get(id=order_id)
        subject = f'Order nr. {order.id}'
        message = f'Cher {order.prénom},\n\n' \
                f'You have successfully placed an order.' \
                f'Votre numéro de Commande est: {order.id}.'
        mail_sent = send_mail(subject,
                                message,
                                'admin@kds.com',
                                [order.email])
        return mail_sent
