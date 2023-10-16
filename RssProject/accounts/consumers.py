import pika
import json

from interactions.models import CustomUser, Notif, UserNotif



def callback(ch, method, property, body):
    body = json.loads(body)
    user = CustomUser.objects.get(username=body["username"])
    notif = Notif.objects.create(message=body["message"], status=body["status"])
    UserNotif.objects.create(user=user, notification=notif)
    ch.basic_ack(delivery_tag=method.delivery_tag)




def register_consumer():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
    ch = connection.channel()
    ch.queue_declare(queue='register')
    ch.basic_consume(queue='register', on_message_callback=callback)
    ch.start_consuming()




def login_consumer():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
    ch = connection.channel()
    ch.queue_declare(queue='login')
    ch.basic_consume(queue='login', on_message_callback=callback)
    ch.start_consuming()





def rss_callback(ch, method, property, body):
    body = json.loads(body)
    all_subscribed = SubScribe.objects.all()
    for sub in all_subscribed:
        notif = Notif.objects.create(message=body["message"], status=body["status"])
        user = sub.user
        UserNotif.objects.create(user=user, notification=notif)
    ch.basic_ack(delivery_tag=method.delivery_tag)




def rss_update_consumer():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
    ch = connection.channel()
    ch.queue_declare(queue='UpdateRss')
    ch.basic_consume(queue='UpdateRss', on_message_callback=rss_callback)
    ch.start_consuming()



def rss_parser_consumer():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
    ch = connection.channel()
    ch.queue_declare(queue='ParseRss')
    ch.basic_consume(queue='ParseRss', on_message_callback=rss_callback)
    ch.start_consuming()