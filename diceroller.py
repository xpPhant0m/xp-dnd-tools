import random

def main():
    cmd = input('~')

    if cmd.startswith('rolld'): #eg rolld6
        print(random.randint(1,(int(cmd[5:]))))

    if cmd.startswith('statgen'): #eg statgen6
        for i in range(int(cmd[7:])):
            d6 = [random.randint(1,6) for _ in range(4)]
            d6.remove(min(d6))
            print(sum(d6))

    if cmd == 'h':
        print('rolld -> roll any dice by typing rolld{number}')
        print('statgen -> rolls 4 d6s and removes the lowest')

    return 1

while True:
    main()
