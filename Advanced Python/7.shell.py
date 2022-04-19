import os
from colorama import Fore
import readline

def ls():
    # get current directory
    files = os.getcwd()
    getFiles = os.listdir(files)
    print('\t'.join(getFiles))


def getFileOrFolderName(cmd):
    names = []
    name = cmd[1]
    if len(cmd) > 2:
        for i in range(1, len(cmd)):
            names.append(cmd[i])
        name = f"{' '.join(names)}"

    return name


def cat(cmd):
    with open(getFileOrFolderName(cmd), 'r')as f:
        data = f.read()
    print(data)


def cd(cmd):
    path = getFileOrFolderName(cmd)
    try:
        os.chdir(path)
        # print("Current working directory: {0}".format(os.getcwd()))
    except FileNotFoundError:
        print("Directory: {0} does not exist".format(path))
    except NotADirectoryError:
        print("{0} is not a directory".format(path))
    except PermissionError:
        print("You do not have permissions to change to {0}".format(path))


def mkdir(cmd):
    newFolder = getFileOrFolderName(cmd)
    if os.path.exists(newFolder): 
        print("Folder has already existed!")
    else:
        os.mkdir(newFolder)


def rmdir(cmd):
    folder = getFileOrFolderName(cmd)
    if (not os.path.exists(folder)): 
        print("The folder does not exist!")
    else:
        os.rmdir(folder)


def touch(cmd):
    newFile = getFileOrFolderName(cmd)
    if os.path.exists(newFile): 
        print("File has already existed!")
    else:
        open(newFile, "w")

def remove(cmd):
    file = getFileOrFolderName(cmd)
    if (not os.path.exists(file)):
        print("The file does not exist!")
    else:
        os.remove(file)


def completer(text, state):
    options = [i for i in os.listdir(os.getcwd()) if i.startswith(text)]
    if state < len(options):
        return options[state]
    else:
        return None

readline.parse_and_bind("tab: complete")
readline.set_completer(completer)


while True:
    directory = os.getcwd()
    command = input(Fore.RED + directory + ": ")
    cmd = command.split(" ")
    if cmd[0] == "cat" and len(cmd) >= 2:
        cat(cmd)
    elif cmd[0] == "ls":
        ls()
    elif cmd[0] == "cd" and len(cmd) >= 2:
        cd(cmd)
    elif cmd[0] == "touch" and len(cmd) >= 2:
        touch(cmd)
    elif cmd[0] == "rm" and len(cmd) >= 2:
        remove(cmd)
    elif cmd[0] == "mkdir" and len(cmd) >= 2:
        mkdir(cmd)
    elif cmd[0] == "rmdir" and len(cmd) >= 2:
        rmdir(cmd)