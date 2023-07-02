import pika, json, os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MovieRatings.settings")
django.setup()

params = pika.URLParameters('amqps://rolhknxb:uNyaxDf7Ko-3alv4QBLJN8j4_8DKx5Uo@gull.rmq.cloudamqp.com/rolhknxb')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='movieratings')


def callback(ch, method, properties, body):
    print('Received in admin')


channel.basic_consume(queue='movieratings', on_message_callback=callback, auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()
