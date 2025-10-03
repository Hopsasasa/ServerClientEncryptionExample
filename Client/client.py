import socket, ssl

# The following script is partly based on a comment from Slayerx96 on GitHub 
# (https://gist.github.com/oborichkin/d8d0c7823fd6db3abeb25f69352a5299?permalink_comment_id=4644594#gistcomment-4644594)
#
# The script is made with the use of the library ssl and socket, where ssl is handling the TLS encryption between the server and client.
# Where the socket library is used in conjuction with ssl to form a connection between server and client.

TCP_IP = 'localhost'
TCP_PORT = 7007
BUFFER_SIZE = 1024

def send_message():

    context = ssl._create_unverified_context(ssl.PROTOCOL_TLS_CLIENT) # lets us use an unverified certificate for the server
    context.load_cert_chain(certfile="client.crt", keyfile="client.key")
    context.load_verify_locations(cafile="client.crt")

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client = context.wrap_socket(sock, server_hostname=TCP_IP) # wrapping the connection in a TLS encryption method
    sock.close()

    client.connect((TCP_IP, TCP_PORT))

    while True:
        message = input("Write encrypted message (close for breaking conn and kill for server termination):\n")
        byte_message = bytearray(message, "utf-8")
        client.send(byte_message) # the encryption of the message is handled by the ssl library
        data = client.recv(BUFFER_SIZE) # the decryption of the received message is handled by the ssl library
        print("received data:", data)
        if message == "close" or message == "kill":
            break
    client.close()

if __name__ == "__main__":
    send_message()