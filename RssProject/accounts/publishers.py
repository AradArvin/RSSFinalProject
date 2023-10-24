import pika
import json



def publisher(log_data: dict) -> None:

    connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
    channel = connection.channel()

    routing_key = log_data["status"]
    body = json.dumps(log_data)
    properties = pika.BasicProperties(delivery_mode=2)

    channel.queue_declare(queue=routing_key)
    channel.basic_publish(exchange='', routing_key=routing_key, body=body, properties=properties)

    connection.close()

