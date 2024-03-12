# import random
import os
import sys
import importlib.util
import re
from pathlib import Path
from runpy import run_path

# imports are needed for some file manipulation stuff

home = str(Path.home())
RUNNING = True
verbose = False
found_envs = []
os.system("touch /tmp/vsdm")


def printred(skk):
    print("\033[91m {}\033[00m".format(skk))


def printgreen(skk):
    print("\033[92m {}\033[00m".format(skk))


def printyellow(skk):
    print("\033[93m {}\033[00m".format(skk))


def printlightpurple(skk):
    print("\033[94m {}\033[00m".format(skk))


def printpurple(skk):
    print("\033[95m {}\033[00m".format(skk))


def printcyan(skk):
    print("\033[96m {}\033[00m".format(skk))


def printlightgray(skk):
    print("\033[97m {}\033[00m".format(skk))


def printblack(skk):
    print("\033[98m {}\033[00m".format(skk))


def printv(skk):
    if verbose:
        printyellow(skk)
    else:
        pass


# this is super not how id do it but its compact so i stole it anyway lmao
# i took this from geeks for geeks
try:
    arguments = sys.argv[1]
except:
    arguments = "-h"
available_commands = [
    [
        "--help, -h",
        "prints info and exits",
    ],
    #
    [
        "--verbose, -v",
        "prints an excessive amount of extra info for diagonostics",
    ],
    #
    [
        "--list, -l",
        " prints all available enviornments and exits",
    ],
    #
    [
        "--list-multi, -m",
        "prints all enviornments with multiple compositors and exits",
    ],
    #
    [
        "--list-wayland, -w",
        "prints installed wayland enviornments (compositors) and exits",
    ],
    #
    [
        "--list-x11, -x",
        "prints installed x11 enviornments and exits",
    ],
    [
        "--make-configs",
        "automatically makes the needed files and folders needed for the program",
    ],
]


def argument_parsing():
    global verbose
    for arg in sys.argv:
        if arg == "-h" or arg == "--help" or arguments == "-h":
            terminal_rows, terminal_columns = os.popen("stty size", "r").read().split()
            # odd placement because its only needed here
            for x in available_commands:
                description = x[1].rjust(int(terminal_columns) - len(x[0]), " ")
                print(f"{x[0]}{description}")
            exit()
        elif arg == "-v" or arg == "verbose":
            verbose = True
        elif arg == "-l" or arg == "--list":
            check_available_envs()

        elif arg == "-m" or arg == "--list-multi":
            print(known_enviornments)
        elif arg == "-x" or arg == "--list-x11":
            pass
        elif arg == "-w" or arg == "--list-wayland":
            pass
        else:
            pass


def config_manager():
    try:
        printv("checking for conf file in home conf folder...")
        run_path(home + "/.config/vsdm/config.py")
        printv("success!")
        printgreen("\nUsing User Config!\n")

    except:
        try:
            import fail

            printv("checking for conf file in etc conf folder...")
            run_path("/etc/vsdm/config.py")
            printyellow(
                "\nUsing Global Config, please use user config when possible!\n"
            )
            printv("success!")
        except:
            printv("both external configs failed, using the local backup...")
            printred(
                "\nfailed to import config," + "please update user or global config!\n"
            )
            print("using default settings!\n")

            user_settings = {
                "qtile_default": "wayland",
                "kde_default": "wayland",
                "plasma_default": "wayland",
                "kwin_default": "wayland",
                "gnome_default": "wayland",
                "mutter_default": "wayland",
                "enlightenment_default": "x11",
                "mate_default": "x11",
            }


known_enviornments = [
    # x11 & wayland
    "qtile",
    "kde",
    "plasma",
    "gnome",
    "enlightenment",
]


def find_env():
    for x in list(enumerate(known_enviornments)):
        if arguments == x[1]:
            known_enviornments[x[0]] = True
            printv(x[1] + " true!")
        else:
            known_enviornments[x[0]] = False
            printv(x[1] + " false...")


def options_checker():
    if any(known_enviornments):
        printv("arguments = " + str(sys.argv))
    else:
        printred("invalid option, format:\n        usdm <enviornment> <opt args>")
        exit()


def xinitrc_manager(enviornment):
    printv("cheking xinitrc...")
    with open(home + "/.xinitrc", "r+") as f:
        printv("current xinit = " + f.read())
        f.close()


# print(home) # /home/zomb
def check_available_envs():
    printv("checking for desktop files...")
    os.system(
        "cat $(ls /usr/share/wayland-sessions/*;"
        " ls /usr/share/xsessions/*) |"
        " grep --word-regexp Exec > /tmp/vsdm"
    )
    # I'm going to try to recreate this with python only,
    # I was able to before, but it was very bad code and
    # wrote to disk more than this does.

    printv("success!")


def something():
    with open("/tmp/vsdm", "r") as desktops:
        print(desktops.read())
        desktops.close


def __main__():
    something()
    argument_parsing()
    try:
        check_available_envs()
    except:
        printred(
            "\nchecking for your desktops has failed "
            "check /usr/share/xsessions for x11 or "
            "/usr/share/wayland-sessions for wayland"
        )
        exit(1)
    find_env()
    options_checker()
    config_manager()
    try:
        xinitrc_manager(sys.argv[1])
    except:
        printred("something has gone very wrong!")


__main__()
