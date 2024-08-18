import socket
import os
import mimetypes

def handle_request(client_socket):
    try:
        request = client_socket.recv(1024).decode()
        print("Request received:")
        print(request)
        
        if not request:
            return
        
        lines = request.split('\n')
        if len(lines) < 1:
            return
        
        request_line = lines[0].split(' ')
        if len(request_line) < 3:
            return
        
        request_file = request_line[1]
        
        if request_file == '/':
            request_file = '/index.html'
        file_path = '.' + request_file

        mime_type, _ = mimetypes.guess_type(file_path)

        if os.path.isfile(file_path):
            with open(file_path, 'rb') as file:
                content = file.read()
            response = 'HTTP/1.1 200 OK\n'
            response += f'Content-Type: {mime_type or "application/octet-stream"}\n'
            response += f'Content-Length: {len(content)}\n'
            response += 'Connection: close\n\n'
            client_socket.send(response.encode() + content)
        else:
            response = 'HTTP/1.1 404 Not Found\n'
            response += 'Content-Type: text/html\n'
            response += 'Connection: close\n\n'
            response += '<html><body><h1>404 Not Found</h1></body></html>'
            client_socket.send(response.encode())
        
    except Exception as e:
        print(f"Error handling request: {e}")
        response = 'HTTP/1.1 500 Internal Server Error\n'
        response += 'Content-Type: text/html\n'
        response += 'Connection: close\n\n'
        response += '<html><body><h1>500 Internal Server Error</h1></body></html>'
        client_socket.send(response.encode())
    
    finally:
        client_socket.close()

def start_server(port=8080):
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(('0.0.0.0', port))
        server_socket.listen(1)
        print(f'Servidor ouvindo na porta {port}...')

        while True:
            client_socket, _ = server_socket.accept()
            handle_request(client_socket)
    
    except Exception as e:
        print(f"Server error: {e}")

if __name__ == "__main__":
    start_server()
