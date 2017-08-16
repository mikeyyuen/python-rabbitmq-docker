import time
import pika

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    time.sleep(body.count(b'.'))
    print(" [x] Done")
    ch.basic_ack(delivery_tag = method.delivery_tag)

credentials = pika.PlainCredentials('admin', 'PLdiJeduXtPc7M')
parameters  = pika.ConnectionParameters(host='rabbitmq.slipstream-test.com', port=5672, 
                                        virtual_host='/', 
                                        credentials=credentials,
                                        ssl=True)

connection = pika.BlockingConnection(parameters)
channel = connection.channel()

#channel.queue_delete(queue='task_queue')
channel.queue_declare(queue='task_queue', durable=True)
channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback, queue='task_queue')

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()

connection.close()
