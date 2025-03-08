import cowsay
from io import StringIO


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

field = [[0 for j in range(10)] for i in range(10)]
allowed_list = cowsay.list_cows()
user_list = {'jgsbat': jgsbat}


def encounter(x, y):
    out = field[y][x].split()
    hello = out[1]
    name = out[0]

    if name in allowed_list:
        print(cowsay.cowsay(hello, cow=name))
    else:
        print(cowsay.cowthink(hello, cowfile=jgsbat))


x, y = 0, 0

while inp := input():
    inp = inp.split()

    moved = 0
    if inp[0] == 'up':
        y = (y - 1) % 10
        moved = 1
    elif inp[0] == 'down':
        y = (y + 1) % 10
        moved = 1
    elif inp[0] == 'right':
        x = (x + 1) % 10
        moved = 1
    elif inp[0] == 'left':
        x = (x - 1) % 10
        moved = 1

    if moved == 1:
        print(f'Moved to ({x}, {y})')

        if field[y][x] != 0:
            encounter(x, y)
    else:
        if inp[0] == 'addmon':
            if len(inp) < 5:
                print("Invalid arguments")
                continue

            try:
                m_x = int(inp[2])
                m_y = int(inp[3])

                if m_x < 0 or m_x > 9 or m_y < 0 or m_y > 9:
                    raise Exception
            except Exception:
                print("Invalid arguments")
                continue

            if inp[1] not in allowed_list and inp[1] not in user_list:
                print("Invalid arguments")
                continue

            if field[m_y][m_x] == 0:
                print(f'Added monster to ({m_x}, {m_y}) saying {inp[4]}')
            else:
                print(f'Replaced the old monster')

            field[m_y][m_x] = inp[1] + ' ' + inp[4]

        else:
            print('Invalid command')
