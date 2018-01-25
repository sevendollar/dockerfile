def collision(nextX, state):
    nextY = len(state)
    for i in range(nextY):
        if abs(state[i] - nextX) in (0, nextY - i):
            return True
    return False


def queen(state=(), number=8):
    for position in range(number):
        if not collision(nextX=position, state=state):
            if len(state) != number - 1:
                for result in queen(number=number, state=state + (position, )):
                    yield (position, ) + result
            else:
                yield (position, )

def print_result(result):
    for i in range(len(result)):
        print('. ' * result[i] + 'Q' + ' .' * (len(result) - result[i] - 1))

import random

s = random.choice(list(queen()))
print(s)
print_result(s)
