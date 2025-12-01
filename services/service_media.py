#!/usr/bin/env python
import pika
import time

# Conexão com RabbitMQ
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost')
)

channel = connection.channel()

# Fila RPC específica da média
channel.queue_declare(queue='rpc_media')


def calcular_media(numeros):
    return sum(numeros) / len(numeros)


def on_request(ch, method, props, body):
    # Converte "2,4,6" → [2, 4, 6]
    numeros = list(map(int, body.decode().split(",")))

    print(f"[.] Recebido para média: {numeros}")
    print("[.] Processando... (5 segundos)")

    # Delay ANTES da resposta
    time.sleep(5)

    resultado = calcular_media(numeros)

    # Envia resultado após os 5s
    ch.basic_publish(
        exchange='',
        routing_key=props.reply_to,
        properties=pika.BasicProperties(
            correlation_id=props.correlation_id
        ),
        body=str(resultado)
    )

    ch.basic_ack(delivery_tag=method.delivery_tag)


# Importantíssimo para balanceamento entre workers
channel.basic_qos(prefetch_count=1)

# Consumidor RPC
channel.basic_consume(
    queue='rpc_media',
    on_message_callback=on_request
)

print(" [x] Aguardando requisições RPC de média...")
channel.start_consuming()
