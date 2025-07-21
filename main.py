from modules import port_scanner, brute_forcer

def main():
    print("=== PENETRATION TESTING TOOLKIT ===")
    print("1. Port Scanner")
    print("2. Brute Force Login (basic HTTP auth)")
    choice = input("Select a module to run (1/2): ")

    if choice == "1":
        target = input("Enter target IP or domain: ")
        port_scanner.scan_ports(target)
    elif choice == "2":
        url = input("Enter target login URL: ")
        username = input("Enter username to brute-force: ")
        wordlist = "wordlists/common_passwords.txt"
        brute_forcer.http_brute_force(url, username, wordlist)
    else:
        print("[!] Invalid choice.")

if __name__ == "__main__":
    main()
