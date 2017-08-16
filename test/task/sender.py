import sys
import pika

credentials = pika.PlainCredentials('admin', 'PLdiJeduXtPc7M')
parameters  = pika.ConnectionParameters(host='rabbitmq.slipstream-test.com', port=5672, 
                                        virtual_host='/', 
                                        credentials=credentials,
                                        ssl=True)

connection = pika.BlockingConnection(parameters)
channel = connection.channel()
channel.queue_declare(queue='task_queue', durable=True)

message = ' '.join(sys.argv[1:]) or "Hello World!"
channel.basic_publish(exchange='',
                      routing_key='task_queue',
                      body=message,
                      properties=pika.BasicProperties(
                         delivery_mode = 2, # make message persistent
                      ))
print(" [x] Sent %r" % message)

connection.close()
