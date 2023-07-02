import pika, json

params = pika.URLParameters('amqps://rolhknxb:uNyaxDf7Ko-3alv4QBLJN8j4_8DKx5Uo@gull.rmq.cloudamqp.com/rolhknxb')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)
