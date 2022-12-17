#!/usr/bin/env python

## from https://www.reddit.com/r/Fedora/comments/3bssp9/how_do_i_run_a_script_on_power_state_change/
## from https://askubuntu.com/questions/183516/how-do-i-detect-when-my-system-wakes-up-from-suspend-via-dbus-or-similar-in-a-py

#!/bin/env python

import dbus      # for dbus communication (obviously)
import gobject   # main loop
from dbus.mainloop.glib import DBusGMainLoop # integration into the main loop

def handle_power_state_change(*args, **kwargs):
     if args[1]['Online'] == 0:
         print("unplugged")
     else:
         print("plugged in")

DBusGMainLoop(set_as_default=True) # integrate into main loob
bus = dbus.SystemBus()             # connect to dbus system wide
bus.add_signal_receiver(           # defince the signal to listen to
    handle_power_state_change,        # name of callback function
    signal_name='PropertiesChanged',                        # singal name
    dbus_interface='org.freedesktop.DBus.Properties',          # interface
    path='/org/freedesktop/UPower/devices/line_power_AC'           # bus name
)

loop = gobject.MainLoop()          # define mainloop
loop.run()                         # run main loop
