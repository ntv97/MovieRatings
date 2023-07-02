import pika, json


params = pika.URLParameters('amqps://rolhknxb:uNyaxDf7Ko-3alv4QBLJN8j4_8DKx5Uo@gull.rmq.cloudamqp.com/rolhknxb')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='main')


def callback(ch, method, properties, body):
    print('Received in main')
    data = json.loads(body)
    print(data)

    if properties.content_type == 'movie_created':
        print('Movie Created')

    elif properties.content_type == 'rating_added':
        print('Rating')

    elif properties.content_type == 'product_deleted':
        print('Movie Deleted')


channel.basic_consume(queue='main', on_message_callback=callback, auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()
