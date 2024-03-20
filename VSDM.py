# import random
import os
import sys
#import importlib.util
from re import split
from pathlib import Path
from runpy import run_path

# imports are needed for some file manipulation stuff

desktop_path = Path("/usr/share/")
home = str(Path.home())
RUNNING = True
verbose = False
found_envs = []
os.system("touch /tmp/vsdm")
known_enviornments = []
x11_desktops = ""
wayland_desktops = ""
env_checker_list = []


def printred(skk):
    print("\033[91m {}\033[00m".format(skk))


def printgreen(skk):
    print("\033[92m {}\033[00m".format(skk))


def printyellow(skk):
    print("\033[93m {}\033[00m".format(skk))


# this is super not how id do it but its compact so i stole it anyway lmao
# i took this from geeks for geeks


def printv(skk):
    if verbose:
        printyellow(skk)
    else:
        pass


try:
    arguments = sys.argv[1]
except:
    arguments = "-h"

available_commands = [
    [
        "--help, -h",
        "prints info and exits",
    ],
    [
        "--verbose, -v",
        "prints an excessive amount of extra info for diagonostics",
    ],
    [
        "--list, -l",
        " prints all available enviornments and exits",
    ],
    [
        "--list-multi, -m",
        "prints all enviornments with multiple compositors and exits",
    ],
    [
        "--list-wayland, -w",
        "prints installed wayland enviornments (compositors) and exits",
    ],
    [
        "--list-x11, -x",
        "prints installed x11 enviornments and exits",
    ],
    # [
    #     "--make-configs",
    #     "makes the needed files and folders needed for the program",
    # ],
]


def argument_parsing():
    global verbose
    for arg in sys.argv:
        arg = str(arg)
        if arg == "-h" or arg == "--help" or arguments == "-h":
            term_rows, term_columns = os.popen("stty size", "r").read().split()
            for x in available_commands:
                description = x[1].rjust(int(term_columns) - len(x[0]), " ")
                print(f"{x[0]}{description}")
            exit()
        elif arg == "-l" or arg == "--list":
            print("available enviornments:")
            check_available_envs()
            for x in x11_desktops + wayland_desktops:
                print("    " + x.stem)
            exit()
            check_available_envs()
        elif arg == "-m" or arg == "--list-multi":
            print(known_enviornments)
            exit()
        elif arg == "-x" or arg == "--list-x11":
            print("available x11 enviornments:")
            check_available_envs()
            for x in x11_desktops:
                print("    " + x.stem)
            exit()
        elif arg == "-w" or arg == "--list-wayland":
            check_available_envs()
            print("available wayland enviornments:")
            for x in wayland_desktops:
                print("    " + x.stem)
            exit()
        # elif arg == "--make-configs":
        #     print("nonfunc")
        #     exit()
        #     open(f"")
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

            printv("checking for conf file in etc conf folder...")
            run_path("/etc/vsdm/config.py")
            printyellow(
                "\nUsing Global Config, please use user config when possible!\n"
            )
            printv("success!")
        except:
            printv("both external configs failed, using the local backup...")
            printred(
                "\nfailed to import config," "please update user or global config!\n"
            )
            print("using default settings!\n")

            user_settings = {
                "qtile_default": "wayland",
                "plasma_default": "wayland",
                "gnome_default": "wayland",
                "enlightenment_default": "x11",
                "mate_default": "x11",
            }


known_enviornments = [
    # x11 & wayland
    "qtile",
    "plasma",
    "gnome",
    "enlightenment",
    "mate",
]

def multi_env_checker():
    global wayland_desktops, x11_desktops
    for desktop in  wayland_desktops + x11_desktops:
        for x in known_enviornments:
            if desktop == x:
                desktop = ""
        pass
    
def find_chosen_env():
    x11_options = []
    wayland_options = []
    for x in wayland_desktops:
        wayland_options.append(str(x.stem))
    for x in x11_desktops:
        x11_options.append(str(x.stem))
    for x in list(enumerate(known_enviornments)):
        if arguments == x[1]:
            env_checker_list.append(True)
            printv(x[1] + " true!")
            break
        else:
            env_checker_list.append(False)
            printv(x[1] + " false...")
            #make this a function
        if any(env_checker_list):
            for x in list(enumerate(wayland_options)):
                if arguments == x[1][0]:
                    env_checker_list.append(True)
                    env = 
                    printv(x[1][0] + " true!")
                    break
                else:
                    env_checker_list.append(False)
                    printv(x[1][0] + " false...")
                    #make this a function
                    
        if any(env_checker_list):
            for x in list(enumerate(x11_options)):
                if arguments == x[1][0]:
                    env_checker_list.append(True)
                    printv(x[1][0] + " true!")
                    break
                else:
                    env_checker_list.append(False)
                    printv(x[1][0] + " false...")


def options_checker():
    if any(env_checker_list):
        printv("arguments = " + str(sys.argv))
    else:
        printred("invalid option, format:" "\n        usdm <enviornment> <opt args>")
        exit()


def xinitrc_manager(enviornment):
    printv("cheking xinitrc...")
    with open(home + "/.xinitrc", "r+") as f:
        printv("current xinit = " + f.read())
        f.close()


# print(home) # /home/zomb
def check_available_envs():
    global wayland_desktops
    global x11_desktops
    printv("checking for desktop files...")
    try:
        printv("    x11...")
        x11_desktops = list(desktop_path.glob("xsessions/*"))
        printv("   success!")
    except:
        printv(
            "x11 desktop file search failed, you "
            "might either have improperly set permissions "
            "or no xsessions"
        )
    try:
        printv("    wayland...")
        wayland_desktops = list(desktop_path.glob("wayland-sessions/*"))
        printv("   success!")
    except:
        printv(
            "wayland desktop file search failed, you "
            "might either have improperly set permissions "
            "or no wayland sessions"
        )

def check_exec():
    pass
    # printv("opening .desktop file...") # 
    # if chosen_env[1] == "wayland":
    #     with open("/usr/share/", "r") as desktops:
    #         enviornments = re.split("\n", str(desktops.read()))
    #         printv("enviornments" + str(enviornments))
    #         printv("sucess!")
    #         desktops.close


def v_card():
    global verbose
    for arg in sys.argv:
        if arg == "-v" or arg == "--verbose":
            verbose = True

def env_filter(local_list):
        if arguments == x[1][0]:
            env_checker_list.append(True)
            printv(x[1][0] + " true!")
        else:
            env_checker_list.append(False)
            printv(x[1][0] + " false...")


def __main__():
    v_card()
    check_exec()
    argument_parsing()
    try:
        check_available_envs()
    except:
        printred(
            "\nchecking for your desktops has failed"
            "\ncheck /usr/share/xsessions for x11 or"
            "\n/usr/share/wayland-sessions for wayland,"
            "\nif both are there and have .desktop files"
            "\nplease report issue with -v and the needed"
            "\nsteps to recreate at"
            "\n\n    https://github.com/Hecksboi/VSDM/issues"
        )
        exit(1)
    find_chosen_env()
    options_checker()
    config_manager()
    try:
        xinitrc_manager(sys.argv[1])
    except:
        printred(
            "something has gone very wrong!"
            "\nplease report an issue with -v"
            "and the steps neeeded to recreate at"
            "\n    https://github.com/Hecksboi/VSDM/issues"
        )
        exit(1)


__main__()
