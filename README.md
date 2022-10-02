# P2P_CDN
This program is a CDN P2P file sharing system, in which peers who wish to download a file that they do have in their local hard drive, may download it from another active peer who does.

# Instruction
This system includes all the features and functionalities described in the requirements. There are two .py files in the root directory, server.py and client.py. They are used to start the applications for server and peers accordingly.

# How to Run
Setup Server Run server.py directly. Ctrl + C to shutting down the server.
> python3 server.py

![WhatsApp Image 2022-10-02 at 10 11 48 AM](https://user-images.githubusercontent.com/90498262/193439377-798091de-3fb7-4a04-b899-ce78ee101256.jpeg)

Simulate Clients Each client.py starts an application for one client. To run mulpiple clients, copy client.py to different directory. Server's host is optional. It will be localhost by default.
> python3 client.py

![WhatsApp Image 2022-10-02 at 10 11 37 AM](https://user-images.githubusercontent.com/90498262/193439379-bc5623a0-abc3-4269-8516-5ed6200f6e25.jpeg)
 
