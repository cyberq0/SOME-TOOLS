import scapy.all as scapy
import socket
from barcode import EAN13
from barcode.writer import ImageWriter
import qrcode
import secrets
import string
import itertools
import phonenumbers
from phonenumbers import geocoder, timezone
import dns.resolver


def ip_scanner(ip):
    try:
        socket.inet_aton(ip)
        print(f"{ip} is a valid IP address")
    except socket.error:
        print(f"{ip} is not a valid IP address")


def port_scan(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"Port {port} is open")
        sock.close()
    except socket.error:
        print(f"Error scanning port {port}")

def generate_barcode(data):
    ean = EAN13(data, writer=ImageWriter())
    ean.save("barcode")


def generate_qrcode(data):
    img = qrcode.make(data)
    img.save("qrcode.png")


def generate_password(length):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet) for _ in range(length))
    return password


def generate_wordlist(charset, length):
    wordlist = [''.join(p) for p in itertools.product(charset, repeat=length)]
    return wordlist


def get_phone_info(phone_number):
    phone_number_obj = phonenumbers.parse(phone_number, "IN")
    return dict(country_code=phone_number_obj.country_code, national_number=phone_number_obj.national_number,
                carrier=geocoder.description_for_number(phone_number_obj, "en"),
                geolocation=geocoder.description_for_number(phone_number_obj, "en"),
                timezone=timezone.time_zones_for_number(phone_number_obj))


def check_subdomain(domain):
    try:
        answers = dns.resolver.resolve(domain, "A")
        return [answer.to_text() for answer in answers]
    except dns.resolver.NoAnswer:
        return []


def ddos_attack(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"DDoS attack on {ip}:{port} successful")
        else:
            print(f"DDoS attack on {ip}:{port} failed")
        sock.close()
    except socket.error:
        print(f"Error performing DDoS attack on {ip}:{port}")


def main() -> object:
    print("____________________________________________________")
    print("|                                                  |")
    print("|                                                  |")
    print("|  . . . . . . . . . .  . .1 . . . . . . . . . .  |")
    print("|  .       S       .       T       .       O       .  |")
    print("|  .       T       .       O       .       P       .  |")
    print("|  . . . . . . . . . . . . . . . . . . . . . .  |")
    print("|                                                  |")
    print("____________________________________________________")
    print("Recon and Information Gathering Tool")
    print("-------------------------------")
    print("1. IP Scanner")
    print("2. Port Scanner")
    print("3. Barcode Generator")
    print("4. QRCode Generator")
    print("5. Password Generator")
    print("6. Wordlist Generator")
    print("7. Phone number ")
    print("8. Subdomain Checker")
    print("9. DDoS Attack Tool")
    print("-------------------------------")

    choice = input("Enter the number of the tool you want to use: ")

    if choice == "1":
        ip = input("Enter the IP address to scan: ")
        print(ip_scanner(ip))
    elif choice == "2":
        ip = input("Enter the IP address to scan: ")
        start_port = int(input("Enter the start port: "))
        end_port = int(input("Enter the end port: "))
        for port in range(start_port, end_port + 1):
            port_scan(ip, port)
    elif choice == "3":
        data = input("Enter the data to generate a barcode: ")
        generate_barcode(data)
    elif choice == "4":
        data = input("Enter the data to generate a QR code: ")
        generate_qrcode(data)
    elif choice == "5":
        length = int(input("Enter the length of the password to generate: "))
        print(generate_password(length))
    elif choice == "6":
        charset = input("Enter the charset for the wordlist: ")
        length = int(input("Enter the length of the wordlist: "))
        print(generate_wordlist(charset, length))
    elif choice == "7":
        phone_number = input("Enter the phone number: ")
        print(get_phone_info(phone_number))
    elif choice == "8":
        domain = input("Enter the domain to check for subdomains: ")
        print(check_subdomain(domain))
    elif choice == "9":
        ip = input("Enter IP address: ")
        port = int(input("Enter port number: "))
        ddos_attack(ip, port)
    else:
        print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
