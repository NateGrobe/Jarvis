from plugin import plugin
import os
import subprocess
import numbers
# import psutil

@plugin("ram")
def playMusic(jarvis, s): 

    print()
    print("--------------------------------------------------")
    os.system('free >> memory.txt')
    reader = open('memory.txt', 'r')
    memory = reader.readline()

    memory = reader.readline()    
    print("Total memory: ", end = '')
    for i in range(len(memory)):
        if memory[i].isdigit():
            print(memory[i], end = '')
            if memory[i+1] == ' ':
                break
    print()

    print("Used memory: ", end = '')
    memory = reader.readline()
    for i in range(len(memory)):
        if memory[i].isdigit():
            print(memory[i], end = '')
            if memory[i+1] == ' ':
                break
    print()
    os.system('rm memory.txt')
    reader.close()

    os.system('ps >> memory.txt')
    print("Number of currently running processes: ", end = '')
    process = open('memory.txt', 'r')
    lines = process.readlines()
    count = 0
    for line in lines: 
        count += 1
    print(count-1)

    pid = os.getpid()
    ppid = os.getppid()
    for line in lines: 
        for word in line.split():
            if word == str(pid):
                print("Current Process: ", end = '')
                print(line, end = '')
            if word == str(ppid): 
                print("Parent Process: ", end = '')
                print(line, end = '')
    
    process.close()
    os.system('rm memory.txt')
    print("--------------------------------------------------")
    print()