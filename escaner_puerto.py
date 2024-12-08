import socket

# Solicitar la IP al usuario
ip = input("Ingresa la dirección IP a escanear: ")

# Validar rango de puertos
try:
    puerto_inicio = int(input("Puerto inicial (1-65535): "))
    puerto_fin = int(input("Puerto final (1-65535): "))
    if not (1 <= puerto_inicio <= 65535) or not (1 <= puerto_fin <= 65535) or puerto_inicio > puerto_fin:
        raise ValueError("Rangos de puertos inválidos.")
except ValueError as e:
    print(f"Error: {e}")
    exit()

# Escaneo de puertos
print(f"Escaneando la IP {ip} en el rango de puertos {puerto_inicio}-{puerto_fin}...\n")
for puerto in range(puerto_inicio, puerto_fin + 1):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)  # Tiempo de espera reducido para mayor rapidez

    try:
        result = sock.connect_ex((ip, puerto))
        if result == 0:
            print(f"Puerto abierto: {puerto}")
    except Exception as e:
        print(f"Error al escanear el puerto {puerto}: {e}")
    finally:
        sock.close()

print("\nEscaneo completado.")
