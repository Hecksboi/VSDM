# THIS DOES NOT WORK YET

#### Very Simple Desktop Manager

what is this for?
people who want the absolute minimum for their desktop management,
less stuff to manage,the less stuff to worry about.

some things this program will not have are
* 1.user login (this is intended to do as little as possible, use agetty login)
* 2.proper GUI (i might do TUI, but unless theres a hyper minimal DRM option, no GUI in the base)

this project uses the [black formater](https://github.com/psf/black),
depends on sh, (optionally) startx (needed for x11 desktops), and assumes
that you have the dirs ``/tmp/``, ``/usr/share/xsessions/``, 
``/usr/share/wayland-sessions/``, and ``~/.local/bin/``
hopefully i can figure out a better way of starting x11 desktops
