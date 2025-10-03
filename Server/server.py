import socket, ssl

# The following script is partly based on a comment from Slayerx96 on GitHub 
# (https://gist.github.com/oborichkin/d8d0c7823fd6db3abeb25f69352a5299?permalink_comment_id=4644594#gistcomment-4644594)
#
# The script is made with the use of the library ssl and socket, where ssl is handling the TLS encryption between the server and client.
# Where the socket library is used in conjuction with ssl to form a connection between server and client.

TCP_IP = 'localhost'
TCP_PORT = 7007
BUFFER_SIZE = 1024  # Normally 1024, but we want fast response


def start_server():

    print("Starting server!")
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(certfile="server.crt", keyfile="server.key") # load the certificate used by the server
    context.load_verify_locations(cafile="server.crt")

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server = context.wrap_socket(sock) # wrapping the socket connector in the TLS encryption method
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, BUFFER_SIZE)
    sock.close()

    server.bind((TCP_IP, TCP_PORT))
    server.listen(0)

    keepAlive = True
    while keepAlive:
        conn, addr = server.accept()
        print("Connection address:" + str(addr))
        while 1:
            data = conn.recv(BUFFER_SIZE) # the decryption of the received message is handled by the ssl library
            print("received data:", data)
            conn.send(data)  # the encryption of the message is handled by the ssl library
            if data == b'kill': 
                keepAlive = False
                break
            if data == b'close': break
        conn.close()

if __name__ == "__main__":
    start_server()

