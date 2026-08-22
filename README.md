# 🔎 Python Port Scanner

Scanner de portas TCP simples desenvolvido em **Python**, utilizando a biblioteca `socket`.

## 🛠️ Tecnologias

<p align="left">
  <a href="https://www.python.org/">
    <img src="https://skillicons.dev/icons?i=python" height="50" alt="Python"/>
  </a>
</p>

* Python 3
* Socket / TCP
* CLI

## 📁 Estrutura

```text
port-scanner/
└── scanner.py
```

## 🚀 Funcionamento

O programa recebe um IP/hostname e a quantidade de portas a verificar.

Para cada porta, cria uma conexão TCP e identifica se ela está aberta.

```bash
python scanner.py
```

Exemplo:

```text
[*] Enter Target To Scan: 127.0.0.1
[*] Enter how many ports you want to scan: 100
[+] Port Opened 22
[+] Port Opened 80
```

## 📚 Objetivo

Projeto desenvolvido para praticar **Python, sockets, TCP/IP, portas de rede e fundamentos de segurança**.

> ⚠️ Use somente em sistemas e redes nos quais você tenha autorização para realizar testes.
