from colorama import Fore as fore
import os
import sys
import subprocess
import keyboard
def exceute_commands(command):
    try:
       subprocess.run(command.split())
    except Exception:
        print("psh: Command not found: {}" .format(command))


def main():
    rcmd = []
    while True:
        ######
        mydir = os.getcwd()
        command = input(fore.BLUE + mydir + fore.GREEN +  " >>| " + fore.RESET)


        ######
        ## Custom Commands ##
        if command == "exit":
            break

        elif command == "Help":
            rcmd.append(command)
            print("Linux Shell, Written in Python")

        elif command[:2] == "cd":
            try:
                cdi = command[3:]
                os.chdir(cdi)
            except:
                print("cd: " + command[3:] + ": No such file or directory")
        elif command == "rcmds":
            print(rcmd)

        else:
            exceute_commands(command)
main()