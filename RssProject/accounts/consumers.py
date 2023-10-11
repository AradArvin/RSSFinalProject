import pika
import json

from interactions.models import CustomUser, Notif



def callback(ch, method, property, body):
    body = json.loads(body)
    user = CustomUser.objects.get(username=body["username"])
    Notif.objects.create(user=user, message=body["message"], status=body["routing_key"])
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


