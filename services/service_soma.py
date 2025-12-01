#!/usr/bin/env python
import pika
import time

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))

channel = connection.channel()
channel.queue_declare(queue='rpc_soma')


def soma(a, b):
    return a + b


def on_request(ch, method, props, body):
    # Recebe o que o client mandou
    a, b = map(int, body.decode().split(","))

    print(f"[.] Recebido: {a} + {b}")
    print("[.] Processando... (5s)")
    
    # Delay de 5 segundos ANTES da resposta
    time.sleep(5)

    resultado = soma(a, b)

    # Envia a resposta depois do delay
    ch.basic_publish(
        exchange='',
        routing_key=props.reply_to,
        properties=pika.BasicProperties(
            correlation_id=props.correlation_id
        ),
        body=str(resultado)
    )

    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='rpc_soma', on_message_callback=on_request)

print(" [x] Aguardando requisições RPC de soma...")
channel.start_consuming()
