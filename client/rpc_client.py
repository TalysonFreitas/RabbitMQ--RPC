import os
import sys

# Adiciona o diretório raiz ao path
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(ROOT)

from common.rpc_utils import RpcClient

rpc = RpcClient()

while True:
    print("\nEscolha o serviço:")
    print("1 - Soma")
    print("2 - Média")
    print("0 - Sair")

    op = input("> ")

    if op == "0":
        break

    if op == "1":
        a = input("Primeiro número: ")
        b = input("Segundo número: ")
        msg = f"{a},{b}"
        fila = "rpc_soma"

    elif op == "2":
        valores = input("Digite números separados por vírgula: ")
        msg = valores
        fila = "rpc_media"

    else:
        print("Opção inválida.")
        continue

    print(f" [x] Enviando para {fila}...")
    resposta = rpc.call(fila, msg)
    print(f" [.] Resposta: {resposta}")
