# ServerClientEncryptionExample

## Description

This is a short demonstration of how to brute force a simple Elgamal encryption and how to improve upon such a system with TLS encryption.

These scripts are made purely for educational purposes, based on an assigment in the course "Introduction to Security" from the IT University of Copenhagen.

## How to run

### Prerequisites
To run the following examples you need to have python installed on your machine of choice. Depending on your choice of operating system, your python command may differ from the ones written below.

### Elgamal
To run the test of Elgamal bruteforce you need to do the following:

- Start in root of the repository
- Run the command ```python ./bruteforce.py```

### TLS Client-Server
To run the test of TLS encryption between client and server, you need to do the following:

- Create two terminals
- Navigate one of the terminals to the "Server" folder
- Run in the folder ```python ./server.py```
- Navigate the other terminal to the "Client" folder
- Run in the folder ```python ./client.py```

In the client terminal you are then able to send messages to the server and get the same message as response from the server. To kill the client, you can write ```close``` in the client terminal. To kill the server, you can write ```kill``` in the client terminal.



