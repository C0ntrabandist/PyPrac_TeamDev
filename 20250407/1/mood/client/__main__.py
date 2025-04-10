"""Main file for client."""

import sys
import socket
import threading

from . import Mood, recieve


if __name__ == "__main__":
    name = "my name\n" if len(sys.argv) < 2 else sys.argv[1] + "\n"
    host = "localhost" if len(sys.argv) < 3 else sys.argv[2]
    port = 1337 if len(sys.argv) < 4 else int(sys.argv[3])

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(name.encode())
        is_name = s.recv(1024).decode()
        if (is_name[:-1] == "off"):
            print("The name is busy")
            sys.exit(0)

        print(f"{name[:-1]}, Welcome to Python-mood 0.1 !!!")
        mood = Mood(s)

        recieve = threading.Thread(target=recieve, args=(mood,))
        recieve.daemon = True
        recieve.start()

        mood.cmdloop()
