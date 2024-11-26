import pika
import json
from __init__ import *
from calcEngine import *
from set_redis import set_result

def callback(ch, method, properties, body):
    try:
        data = json.loads(body.decode())
        request_id = data.get("request_id")
        expression = data.get("expression")

    except json.JSONDecodeError as e:
        print(f"JSON Decode Error: {e}")

    try:
        result = calc(expression)
        set_result(request_id, result)
        print(f"Result of {expression}: {result}")
        ch.basic_ack(delivery_tag=method.delivery_tag)

    except Exception as e:
        print(f"Error evaluating expression {expression}: {e}") 
        

#####################
# 메시지 소비
#####################
def consume_message():
    credentials = pika.PlainCredentials(USERNAME, PASSWORD)
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=HOST_NAME, credentials=credentials))
    channel = connection.channel()

    channel.basic_consume(queue="calc_queue", on_message_callback=callback, auto_ack=False)

    print("Waiting for messages...")
    channel.start_consuming()
  
if __name__ == "__main__":
        consume_message()