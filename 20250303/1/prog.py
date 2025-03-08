import cowsay
import shlex

field = [[0 for j in range(10)] for i in range(10)]
allowed_list = cowsay.list_cows()
def encounter(x, y):
    print(cowsay.cowsay(field[y][x]['hello'], field[y][x]['name']))
x, y = 0, 0
while inp := input():
    inp = shlex.split(inp)
    moved = 0
    if inp[0] == 'up':

def encounter(x, y):
            encounter(x, y)
    else:
        if inp[0] == 'addmon':
            if len(inp) != 9:
                print("Invalid arguments")
                continue
            name = inp[1]
            hello = ''
            hp = 0
            m_x, m_y = 0, 0
            i = 2
            while i < 9:
                if inp[i] == 'hello':
                    hello = inp[i+1]
                    i += 2
                elif inp[i] == 'hp':
                    try:
                        hp = int(inp[i+1])
                    except Exception:
                        break
                    if hp <= 0:
                        break
                    i += 2
                elif inp[i] == 'coords':
                    try:
                        m_x = int(inp[i+1])
                        m_y = int(inp[i+2])
                    except Exception:
                        break
                    if m_x < 0 or m_x > 9 or m_y < 0 or m_y > 9:
                        break
                    i += 3
                else:
                    print("Invalid arguments")
                    break
            if i < 9:
                continue
            field[m_y][m_x] = {'hello':hello, 'hp': hp, 'name': name}
        else:
            print('Invalid command')
