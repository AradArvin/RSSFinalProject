
def callback(ch, method, property, body):
    body = json.loads(body)
    user = CustomUser.objects.get(username=body["username"])
    Notif.objects.create(user=user, message=body["message"], status=body["routing_key"])
    ch.basic_ack(delivery_tag=method.delivery_tag)



