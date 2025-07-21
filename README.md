# Penetration-Testing-Kit

COMPANY: CODETECH IT SOLUTIONS

NAME: MOHAMMED ADYAN AHMED

INTERN ID: CT04DG2095

DOMAIN: CYBER SECURITY AND ETHICAL HACKING

DURATION: 4 WEEKS

MENTOR: NEELA SANTOSH

##DESCRIPTION

The Penetration Testing Toolkit is a modular Python-based project designed to provide cybersecurity students and ethical hackers with hands-on tools commonly used in network and web application security testing. This toolkit combines multiple essential modules, including a TCP Port Scanner and an HTTP Brute-Force Login Attacker, into a single, extensible framework. Built entirely in Python, the toolkit is both lightweight and flexible, making it ideal for educational environments, demonstrations, and basic penetration testing simulations. The primary goal of this project is to provide users with a foundational understanding of how reconnaissance and exploitation techniques are implemented programmatically and how such tools can be built from scratch. Each module is designed to work independently but is accessible from a centralized launcher script (main.py), which provides a simple menu-driven interface for ease of use. The Port Scanner module uses Python’s socket library to scan a range of TCP ports (by default, ports 1 to 1024) on a target IP or domain, reporting any open ports that could potentially be exploited. This helps users identify active services on a system, which is a crucial step in any security assessment. Meanwhile, the Brute-Force module uses the requests library to automate POST-based login attempts against web applications. It takes a target login URL, a username, and a password wordlist (such as common_passwords.txt) to repeatedly submit credentials until a successful login is detected or the list is exhausted. This simulates how attackers may use brute-force techniques to gain unauthorized access to weakly protected accounts.

The toolkit follows a modular design pattern, with separate Python scripts for each functionality stored in a modules directory, promoting scalability and clean code management. Additional features or tools—such as a subdomain scanner, directory buster, or vulnerability detector—can easily be integrated as new modules by simply writing them in Python and linking them to the main launcher. Another folder, wordlists, is reserved for storing dictionaries and password lists that can be used across different modules. The included wordlist file contains a basic list of common passwords and can be customized or replaced based on the testing scenario. To ensure cross-platform compatibility, the project uses standard Python 3 libraries along with minimal external dependencies (only requests needs to be installed via pip). Execution is user-friendly, especially for beginners using IDLE or command-line interfaces, with clear instructions and prompts to guide the user through each phase of scanning or brute-forcing.

While the toolkit is powerful in its simplicity, it is designed for educational and ethical use only. Users are strongly warned to avoid deploying this toolkit on any website or network they do not own or have explicit permission to test. Unauthorized scanning or brute-force attacks can be illegal and unethical. As such, it is recommended that users test this toolkit in controlled environments like DVWA (Damn Vulnerable Web Application), bWAPP, or on their own systems. Overall, the Penetration Testing Toolkit is not only a practical learning tool for cybersecurity and ethical hacking students but also a solid starting point for anyone interested in building their own custom penetration testing utilities in Python.

##OUTPUT

<img width="766" height="219" alt="462899783-76aeb3c4-e032-4803-b91a-21b50943363a" src="https://github.com/user-attachments/assets/fcd07de2-8835-4be6-9706-ce45a99f00c7" />

<img width="915" height="316" alt="462899837-ef590d75-6572-431f-aad7-3f4c4eae71c7" src="https://github.com/user-attachments/assets/9b76442c-2112-462e-8e4c-10e079ea5363" />

