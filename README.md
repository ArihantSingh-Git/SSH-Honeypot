# 🐝 SSH Honeypot (Python)

An **SSH Honeypot** built using Python that simulates a fake SSH server to capture and log unauthorized access attempts, including usernames, passwords, and commands executed by attackers.

---

## 🚀 Features

* Accepts all login attempts (captures credentials)
* Logs:

  * IP address
  * Username & Password
  * Commands executed
* Simulates a fake Linux shell environment
* Multi-threaded (handles multiple connections)
* Lightweight and easy to deploy

---

## 🛠️ Tech Stack

* Python 3
* Paramiko (SSH library)
* Socket Programming
* Threading

---

## 📁 Project Structure

```
ssh_honeypot/
│── ssh_honeypot.py
│── honeypot.log
│── README.md
```

---

## ⚙️ Installation & Setup (Kali Linux)

### 1. Clone the Repository

```
git clone https://github.com/your-username/ssh-honeypot.git
cd ssh-honeypot
```

### 2. Create Virtual Environment

```
python3 -m venv venv
```

### 3. Activate Environment

```
source venv/bin/activate
```

### 4. Install Dependencies

```
pip install paramiko
```

---

## ▶️ Running the Honeypot

```
python3 ssh_honeypot.py
```

Output:

```
SSH Honeypot Server
Starting honeypot on port 2222...
```

---

## 🧪 Testing the Honeypot

Open another terminal and run:

```
ssh test@localhost -p 2222
```

* Enter any password
* Login will always succeed (honeypot behavior)

---

## 📜 Logs

All activity is stored in:

```
honeypot.log
```

Example log:

```
[LOGIN ATTEMPT] IP: 127.0.0.1 | Username: test | Password: 12345
[COMMAND] IP: 127.0.0.1 | Command: ls
```

---

## ⚠️ Security Disclaimer

This project is for **educational and research purposes only**.

* Do NOT expose this directly to the internet without proper security controls.
* Do NOT run on port 22 (default SSH port).
* Always deploy inside a controlled environment (VM/VPS).

---

## 🔥 Future Enhancements

* 🌍 GeoIP tracking of attackers
* 📊 Real-time dashboard (Flask/FastAPI)
* 🧠 Intelligent command emulation
* 📡 Integration with SIEM tools (Splunk, ELK)
* 🤖 AI-based attacker behavior analysis

---

## 🎯 Learning Outcomes

* Understanding SSH protocol basics
* Working with Paramiko
* Logging and monitoring attacker activity
* Basics of defensive cybersecurity (Blue Team)

---

## 👨‍💻 Author

**Arihant**
Cybersecurity Enthusiast 🚀

---

## ⭐ Contribute

Feel free to fork this repo, improve it, and submit a pull request!

---
