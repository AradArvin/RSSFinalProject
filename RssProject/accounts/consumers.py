import pika
import json

from interactions.models import CustomUser, Notif, UserNotif, SubScribe



def callback(ch, method, property, body):
    body = json.loads(body)
    user = CustomUser.objects.get(username=body["username"])
    notif = Notif.objects.create(message=body["message"], status=body["status"])
    UserNotif.objects.create(user=user, notification=notif)
    ch.basic_ack(delivery_tag=method.delivery_tag)



def rss_callback(ch, method, property, body):
    body = json.loads(body)
    all_subscribed = SubScribe.objects.all()
    for sub in all_subscribed:
        notif = Notif.objects.create(message=body["message"], status=body["status"])
        user = sub.user
        UserNotif.objects.create(user=user, notification=notif)
    ch.basic_ack(delivery_tag=method.delivery_tag)



def consumer_starter(queue: str):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
    ch = connection.channel()
    ch.queue_declare(queue=queue)
    ch.basic_consume(queue=queue, on_message_callback=select_callback(queue))
    ch.start_consuming()

    

def select_callback(queue):
    callback_func = {
        "login": callback,
        "register": callback,
        "UpdateRss": rss_callback,
        "ParseRss": rss_callback
    }
    return callback_func.get(queue)

