import pika

credentials = pika.PlainCredentials('admin', 'PLdiJeduXtPc7M')
parameters  = pika.ConnectionParameters(host='rabbitmq.slipstream-test.com', port=5672, 
                                        virtual_host='/', 
                                        credentials=credentials,
                                        ssl=True)

connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.queue_declare(queue='hello')
channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')
print(" [x] Sent 'Hello World!'")

connection.close()
