import os
import subprocess
import shutil
import time


def ls():
    # get working directory
    loc = os.getcwd()
    c = os.listdir(loc)
    print(c)


def rm(cmd):
    if (len(cmd) == 2):
        file = cmd[1]
        if (file[0] != "/"):
            dir = os.getcwd()
            dirname = dir + "/" + file
            shutil.rmtree(dirname)
            print("remove " + dirname)
    else:
        pass


def cd(cmd):
    loc = cmd[1]
    os.chdir(loc)


def touch(cmd):
    path = cmd[1]
    if (not os.path.exists(path)):
        open(path, "w")


if __name__ == '__main__':
    while True:
        command = input("Enter your command line: \n")
        cmd = command.split(" ")
        if (cmd[0] == "cat"):
            fname = cmd[1]
            with open(fname, 'r')as file:
                data = file.read()
            print(data)
        elif cmd[0] == "ls" and len(cmd) == 1:
            ls()
        # elif cmd[0]=="ls" and len(cmd)==2:
        #     ls2(cmd)
        elif len(cmd) == 2 and cmd[0] == "cd":
            cd(cmd)
        elif cmd[0] == "touch":
            touch(cmd)
        # ps -ef | grep firefox
        elif command.startswith("ps"):
            cmdd = command.split(" | ")
            print("cmdd", cmdd)
            for i in range(len(cmdd)):
                if i == 0:
                    ps = subprocess.Popen(cmdd[i].split(" "), stdout=subprocess.PIPE)
                else:
                    grep = subprocess.Popen(cmdd[i].split(" "), stdin=ps.stdout, stdout=subprocess.PIPE,
                                            encoding='utf-8')
            ps.stdout.close()
            output, _ = grep.communicate()
            python_processes = output.split('\n')
            print(python_processes)
        # bc a.txt or ls -la a.txt or ls -la
        elif len(cmd) > 1:
            print(subprocess.Popen(cmd))
            time.sleep(1)

            # subprocess.run(cmd)