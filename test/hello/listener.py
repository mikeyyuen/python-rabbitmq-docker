import pika

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

credentials = pika.PlainCredentials('admin', 'PLdiJeduXtPc7M')
parameters  = pika.ConnectionParameters(host='db.slipstream-test.com', port=5672, 
                                        virtual_host='/', 
                                        credentials=credentials,
                                        ssl=True)

connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.queue_declare(queue='hello')
channel.basic_consume(callback, queue='hello', no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()

connection.close()
