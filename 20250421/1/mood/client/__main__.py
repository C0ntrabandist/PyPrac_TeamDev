"""Main file for client."""

import sys
import socket
import threading

from . import Mood, recieve


if __name__ == "__main__":
    host = "localhost"
    port = 1337
    name = "My name\n"
    file = ""

    for i in range(len(sys.argv)):
        if sys.argv[i] == '--file':
            file = "" if len(sys.argv) < i + 2 else sys.argv[i + 1]
        elif sys.argv[i] == '--name':
            name = "my name\n" if len(sys.argv) < i + 2 else sys.argv[i + 1] + "\n"
        elif sys.argv[i] == '--host':
            host = 'localhost' if len(sys.argv) < i + 2 else sys.argv[i + 1]
        elif sys.argv[i] == '--port':
            port = 1337 if len(sys.argv) < i + 2 else int(sys.argv[i + 1])

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(name.encode())
        is_name = s.recv(1024).decode()
        if (is_name[:-1] == "off"):
            print("The name is busy")
            sys.exit(0)

        print(f"{name[:-1]}, Welcome to Python-mood 0.1 !!!")
        if file != "":
            fd = open(file, 'r')
            mood = Mood(s, fd)
            mood.prompt = ""
            mood.use_rawinput = False
        else:
            mood = Mood(s)

        recieve = threading.Thread(target=recieve, args=(mood,))
        recieve.daemon = True
        recieve.start()

        mood.cmdloop()
