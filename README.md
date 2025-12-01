# 📘 **Sistema Distribuído com RabbitMQ RPC — Python**

Este projeto implementa um sistema distribuído simples utilizando **RabbitMQ** e o padrão **RPC (Remote Procedure Call)**, baseado no Tutorial 6 do RabbitMQ, mas estendido para suportar múltiplos serviços independentes.

Cada serviço atua como um *servidor RPC* separado, processando requisições específicas.  
O cliente permite escolher qual operação executar e aguarda a resposta do serviço.

---

# 📂 **Estrutura de Pastas**

```
rabbitmq-rpc-distribuido/
│
├── README.md
│
├── client/
│   └── rpc_client.py
│
├── services/
│   ├── service_soma.py
│   └── service_media.py
│
└── common/
    └── rpc_utils.py
```

---

# 🚀 **Componentes do Sistema**

### ✔ `client/rpc_client.py`
Cliente RPC que:
- Exibe menu para escolher operação
- Envia requisições usando RabbitMQ
- Recebe respostas via callback queue

### ✔ `services/service_soma.py`
Serviço RPC para somar dois números.  
Simula tempo de processamento com **delay de 5 segundos**.

### ✔ `services/service_media.py`
Serviço RPC para calcular média de uma lista de números.  
Também inclui **delay de 5 segundos** para demonstrar processamento.

### ✔ `common/rpc_utils.py`
Contém a classe `RpcClient`, usada pelo cliente para enviar requisições RPC e aguardar respostas.

---

# 🧰 **Requisitos**

- Python 3.10+  
- Bibliotecas:
```
pika
```
- RabbitMQ instalado e executando em `localhost`

Instalar dependências:
```bash
pip install -r requirements.txt
```

---

# ▶️ **Como Executar o Sistema**

### **1️⃣ Rodar os serviços (em terminais separados)**

Terminal 1 — Serviço de Soma:
```bash
python services/service_soma.py
```

Terminal 2 — Serviço de Média:
```bash
python services/service_media.py
```

Cada um deles ficará aguardando requisições:

```
[x] Aguardando requisições RPC de soma...
[x] Aguardando requisições RPC de média...
```

---

### **2️⃣ Rodar o cliente**
```bash
python client/rpc_client.py
```

---

# 🖥️ **Exemplo de Execução**

### **No cliente:**
```
Escolha o serviço:
1 - Soma
2 - Média
0 - Sair
> 1
Digite o primeiro número: 4
Digite o segundo número: 7
Enviando requisição para rpc_soma...
Aguardando resposta...
Resposta: 11
```

### **No serviço de soma:**
```
[.] Recebido: 4 + 7
[.] Processando... (5s)
```

---

# 📄 **Licença**
Livre para uso educacional.
