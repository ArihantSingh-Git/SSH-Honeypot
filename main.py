# SSH Honeypot
# Author: Arihant 🚀

import socket
import threading
import paramiko
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    filename="honeypot.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
)

HOST_KEY = paramiko.RSAKey.generate(2048)

BANNER = """
\033[1;32m
╔══════════════════════════════════════╗
║        SSH Honeypot Server 🐝        ║
║          Created by Arihant          ║
╚══════════════════════════════════════╝
\033[0m
"""

class SSHHoneypot(paramiko.ServerInterface):

    def __init__(self, client_ip):
        self.event = threading.Event()
        self.client_ip = client_ip

    def check_auth_password(self, username, password):
        logging.info(f"[LOGIN ATTEMPT] IP: {self.client_ip} | Username: {username} | Password: {password}")
        return paramiko.AUTH_SUCCESSFUL  # Always accept login (trap)

    def check_channel_request(self, kind, chanid):
        if kind == "session":
            return paramiko.OPEN_SUCCEEDED
        return paramiko.OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED

    def check_channel_shell_request(self, channel):
        self.event.set()
        return True


def handle_client(client, addr):
    print(f"[+] Connection from {addr[0]}:{addr[1]}")
    logging.info(f"[NEW CONNECTION] {addr[0]}:{addr[1]}")

    try:
        transport = paramiko.Transport(client)
        transport.add_server_key(HOST_KEY)

        server = SSHHoneypot(addr[0])
        transport.start_server(server=server)

        channel = transport.accept(20)
        if channel is None:
            return

        channel.send("\nWelcome to Ubuntu 22.04 LTS\n")
        channel.send("login successful\n\n")

        while True:
            channel.send("$ ")
            command = channel.recv(1024).decode("utf-8").strip()

            if not command:
                continue

            logging.info(f"[COMMAND] IP: {addr[0]} | Command: {command}")

            if command.lower() in ["exit", "quit"]:
                channel.send("Bye!\n")
                break

            # Fake responses
            if command == "whoami":
                response = "root\n"
            elif command == "uname -a":
                response = "Linux ubuntu 5.15.0-60-generic x86_64\n"
            elif command == "ls":
                response = "bin  etc  home  var  tmp\n"
            else:
                response = "Command not found\n"

            channel.send(response)

        channel.close()

    except Exception as e:
        print(f"[!] Error: {e}")


def start_server(host="0.0.0.0", port=2222):
    print(BANNER)
    print(f"[+] Starting honeypot on port {port}...\n")

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host, port))
    sock.listen(100)

    while True:
        client, addr = sock.accept()
        threading.Thread(target=handle_client, args=(client, addr)).start()


if __name__ == "__main__":
    start_server()