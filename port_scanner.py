import socket
import sys 

target_ip = input("Masukkan Alamat IP Target: ")

print("-" * 50)
print(f"Memindai target: {target_ip}")
print("-" * 50)

try:
    for port in range(1, 1025):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5) 
        
        hasil = s.connect_ex((target_ip, port))
        
        if hasil == 0:
            print(f"Port {port} [TERBUKA]")
            
        s.close()

except KeyboardInterrupt:
    print("\nProses dihentikan.")
    sys.exit()
except socket.gaierror:
    print("\nHostname tidak dapat ditemukan. Coba lagi.")
    sys.exit()
except socket.error:
    print("\nTidak dapat terhubung ke server.")
    sys.exit()

print("-" * 50)
print("Pemindaian Selesai.")