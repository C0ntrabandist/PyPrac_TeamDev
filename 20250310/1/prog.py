import cowsay
import cmd
from io import StringIO
import shlex


class Mud(cmd.Cmd):
    jgsbat = cowsay.read_dot_cow(StringIO("""
    $the_cow = <<EOC;
        ,_                    _,
        ) '-._  ,_    _,  _.-' (
        )  _.-'.|\\--//|.'-._  (
         )'   .'\\/o\\/o\\/'.   `(
          ) .' . \\====/ . '. (
           )  / <<    >> \\  (
            '-._/``  ``\\_.-'
      jgs     __\\'--'//__
             (((""`  `"")))
    EOC
    """))

    prompt = ':->'

    def __init__(self):
        super().__init__()

        self.x = 0
        self.y = 0

        self.field = [[0 for j in range(10)] for i in range(10)]
        
        self.allowed_list = cowsay.list_cows()
        self.user_list = {'jgsbat': self.jgsbat}


    def do_EOF(self, args):
        return True


if __name__ == "__main__":
    print("<<< Welcome to Python-MUD 0.1 >>>")

    Mud().cmdloop()   
