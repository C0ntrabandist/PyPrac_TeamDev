"""Init file for client."""

import cowsay
import cmd
import readline
import shlex
import time
import sys

from ..common import jgsbat, prompt, weapons


class Mood(cmd.Cmd):
    """Class Mood shows the command line, autocomplete attack command and send commands to server."""

    prompt = prompt

    def __init__(self, conn, stdin=sys.stdin):
        """Initialize variables."""
        super().__init__(stdin=stdin)

        self.conn = conn

        self.allowed_list = cowsay.list_cows()
        self.user_list = {'jgsbat': jgsbat}

    def precmd(self, line):
        """Freeze console enter."""
        time.sleep(1)
        return super().precmd(line)

    def do_up(self, args):
        """Send to server message about moving up."""
        self.conn.sendall("move 0 -1\n".encode())

    def do_down(self, args):
        """Send to server message about moving down."""
        self.conn.sendall("move 0 1\n".encode())

    def do_right(self, args):
        """Send to server message about moving to the right."""
        self.conn.sendall("move 1 0\n".encode())

    def do_left(self, args):
        """Send to server message about moving to the left."""
        self.conn.sendall("move -1 0\n".encode())

    def do_addmon(self, args):
        """Send message about adding the monster."""
        self.conn.sendall(("addmon " + args + "\n").encode())

    def do_attack(self, args):
        """Send message about attackin the monster."""
        self.conn.sendall(("attack " + args + "\n").encode())

    def do_sayall(self, args):
        """Send message to all players."""
        self.conn.sendall(("sayall " + args + "\n").encode())

    def complete_attack(self, text, line, begidx, endidx):
        """Complete attack line."""
        res = shlex.split(line[:begidx], 0, 0)

        if len(res) <= 1:
            mon_list = list(self.user_list.keys()) + self.allowed_list
            return [c for c in mon_list if c.startswith(text)]
        elif res[-1] == 'with':
            return [c for c in weapons if c.startswith(text)]

    def do_movemonsters(self, args):
        """End cmd activity."""
        if args != "off" and args != "on":
            print("Invalid command.")

        self.conn.sendall(("movemonsters " + args + "\n").encode())

    def do_q(self, args):
        """End cmd activity."""
        return True

    def do_quit(self, args):
        """End cmd activity."""
        return True

    def do_EOF(self, args):
        """End cmd activity."""
        return True


def recieve(cmd):
    """Recieve the messages from server in another thread."""
    while cmd.conn is not None:
        data = ""

        while len(new := cmd.conn.recv(1024)) == 1024:
            data += new.decode()

        data += new.decode()

        print(f"\n{data.strip()}\n{cmd.prompt}{readline.get_line_buffer()}", end='', flush=True)
