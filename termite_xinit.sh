#!/usr/bin/env bash

# Open termite as X11 environment
/usr/bin/termite --geometry=1280x800 -e "tmux new -s from_xinit"

# Increase the repeat rate of the keyboard
/usr/bin/xset r rate 400 44 &

# Turn off cap locks
/usr/bin/setxkbmap -option caps:none &

# Enable killing X via key combo
/usr/bin/setxkbmap -option terminate:ctrl_alt_bksp &
