# p2p_CDN
This program is a CDN P2P file sharing system, in which peers who wish to download a file that they do have in their local hard drive, may download it from another active peer who does.

#Instruction
This system includes all the features and functionalities described in the requirements. There are two .py files in the root directory, server.py and client.py. They are used to start the applications for server and peers accordingly.

#How to Run
Setup Server Run server.py directly. Ctrl + C to shutting down the server.
python3 server.py

Simulate Clients Each client.py starts an application for one client. To run mulpiple clients, copy client.py to different directory. Server's host is optional. It will be localhost by default.
python3 client.py
