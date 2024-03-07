# import random
import os
import sys
import user_setting as user_settings
from pathlib import Path

home = str(Path.home())
arguments = sys.argv[1]
available_commands = [
    "--help, -h prints info and exits",
    "--verbose, -v prints an excessive amount of extra info for diagonostics (nonfunc)",
    "--list, -l prints all available enviornments and exits",
    "--list-wayland,-w prints wayland enviornments (compositors) and exits",
    "--list-x11, -x prints x11 enviornments and exits",
    "--list-multi, -m prints enviornments with multiple compositors and exits",
]

known_enviornments = [
    # x11 & wayland
    ["qtile", user_settings.qtile_default],
    ["kde", user_settings.kde_default],
    ["plasma", user_settings.plasma_default],
    ["kwin", user_settings.kwin_default],
    ["gnome", user_settings.gnome_default],
    ["mutter", user_settings.gnome_default ],
    ["enlightenment", user_settings.enlightenment_default],
    # x11 only
    ["qtilex11", ""],
    ["budgie", ""],
    ["cinnamon", ""],
    ["enlightenment", ""],
    ["gnomex11", ""],
    ["kdex11", ""],
    ["plasmax11", ""],
    ["lxde", ""],
    ["lxqt", ""],
    ["lumina", ""],
    ["mate", ""],
    ["xfce", ""],
    ["aewm", ""],
    ["aewm++", ""],
    ["amiwm", ""],
    ["awesome", ""],
    ["blackbox", ""],
    ["bspwm", ""],
    ["ctwm", ""],
    ["cwm", ""],
    ["dwm", ""],
    ["echinus", ""],
    ["enlightenment", ""],
    ["evilwm", ""],
    ["fluxbox", ""],
    ["fvwm", ""],
    ["goomwwm", ""],
    ["herbsluftwm", ""],
    ["jwm", ""],
    ["i3", ""],
    ["icewm", ""],
    ["larswm", ""],
    ["lwm", ""],
    ["marco", ""],
    ["muffin", ""],
    ["musca", ""],
    ["notion", ""],
    ["openbox", ""],
    ["oroborus", ""],
    ["page", ""],
    ["pekwm", ""],
    ["ratpoison", ""],
    ["sithwm", ""],
    ["spectrwm", ""],
    ["stumpwm", ""],
    ["twm", ""],
    ["windowlab", ""],
    ["windowmaker", ""],
    ["wm2", ""],
    ["xmonad", ""],
    # wayland only
    ["hikari", ""],
    ["gnomewl", ""],
    ["kdewl", ""],
    ["sway", ""],
    ["wayfire", ""],
    ["cage", ""],
    ["cagebreak", ""],
    ["dwl", ""],
    ["hyprland", ""],
    ["kiwmi", ""],
    ["labwc", ""],
    ["liri", ""],
    ["newwm", ""],
    ["river", ""],
    ["waybox", ""],
    ["weston", ""],
]
for arg in sys.argv[]:
    if arguments == "-h" or if arguments == "--help":
        for x in available_commands[]:
            print(x)
            exit
        
    
for x in list(enumerate(known_enviornments[0][0])):
    if arguments == x[1]:
        known_enviornments[x[0]] = True
    else:
        known_enviornments[x[0]] = False

if any(known_enviornments):
    print(arguments)
else:
    if desktop == "--help" or desktop == "-h":
        print(available_commands)
    print("invalid option, format:\n        usdm <enviornment> <opt args>")

with open(home + "/.xinitrc", "r+") as f:
    print(f.read())
    f.close()
