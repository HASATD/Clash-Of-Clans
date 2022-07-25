
from os import system
from time import sleep,time

file_path = './replays/replay_' + str(1) + '.txt'
replay_file = open(file_path, "r")
lines = replay_file.readlines()

system('clear')
fd = 0
for line in lines:
    fd+=1
    print(line.strip())
    if(fd % 40 == 1):
        sleep(0.5)
        system('clear')
        