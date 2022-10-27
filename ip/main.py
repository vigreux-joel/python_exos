def convert_ip_to_binary(ip):
    return ''.join([bin(int(x) + 256)[3:] for x in ip.split('.')])


def convert_binary_to_ip(binary):
    string = ''
    for i in range(0, len(binary), 8):
        value = binary[i:i + 8]
        string += str(int(value, 2))+"."
    return string[:-1]


def calcul_ip():
    ip = input("Insérer votre adresse IP: ")
    #test: ip = "135.30.34.96/15"

    ip, mask = ip.split('/')
    base = convert_ip_to_binary(ip)[:int(mask)]

    network = str(base) + ("0" * (32 - int(mask)))
    broadcast = str(base) + ("1" * (32 - int(mask)))

    print("Network: " + convert_binary_to_ip(network))
    print("Broadcast: " + convert_binary_to_ip(broadcast))


def main():
    calcul_ip()


if __name__ == '__main__':
    main()
