#!/usr/bin/env python2

'''
Created on 11.03.2010

@author: Arthur Spitzer <arthapex@gmail.com>
'''


import dbus.mainloop.glib
import dbus.service

import gobject

from optparse import OptionParser

app_name = 'mediakeys-daemon'
Version=0.1

DbusBusName = 'org.gnome.SettingsDaemon'
DbusObjectPath = '/org/gnome/SettingsDaemon/MediaKeys'
DbusInterface = 'org.gnome.SettingsDaemon.MediaKeys'

class SettingsDaemonObject(dbus.service.Object):
    def __init__(self, session_bus):
        dbus.service.Object.__init__(self, session_bus, object_path=DbusObjectPath)
        self.__paused = False
        self.__playing = False
        self.__apps = []

    @dbus.service.method(dbus_interface=DbusInterface, in_signature='sd', out_signature='')
    def GrabMediaPlayerKeys(self, app_name, time):
        self.__apps.append(app_name)
    
    @dbus.service.method(dbus_interface=DbusInterface, in_signature='s', out_signature='')
    def ReleaseMediaPlayerKeys(self, app_name):
        self.__apps.remove(app_name)

    @dbus.service.signal(dbus_interface=DbusInterface)
    def MediaPlayerKeyPressed(self, app_name, action):
        pass
    
    def __send_action_to_all_apps(self, action):
        for app in self.__apps:
            self.MediaPlayerKeyPressed(app, action)
    
    @dbus.service.method(dbus_interface=DbusInterface)
    def PressedPlay(self):
        self.__send_action_to_all_apps('Play')
        self.__playing = True
    
    @dbus.service.method(dbus_interface=DbusInterface)
    def PressedPause(self):
        self.__send_action_to_all_apps('Pause')
    
    @dbus.service.method(dbus_interface=DbusInterface)
    def PressedStop(self):
        self.__send_action_to_all_apps('Stop')
    
    @dbus.service.method(dbus_interface=DbusInterface)
    def PressedNext(self):
        self.__send_action_to_all_apps('Next')
    
    @dbus.service.method(dbus_interface=DbusInterface)
    def PressedPrevious(self):
        self.__send_action_to_all_apps('Previous')
    

class Server(object):
    def __init__(self):
        dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)

        session_bus = dbus.SessionBus()
        name = dbus.service.BusName(DbusBusName, session_bus)
        object = SettingsDaemonObject(session_bus)
    
        mainloop = gobject.MainLoop()
        mainloop.run()
    
class Client(object): 
    def __init__(self):
        service = dbus.SessionBus().get_object('org.gnome.SettingsDaemon', '/org/gnome/SettingsDaemon/MediaKeys')
        self.__dbusInterface = dbus.Interface(service, 'org.gnome.SettingsDaemon.MediaKeys')

    def play(self):
        self.__dbusInterface.PressedPlay()
    
    def pause(self):
        self.__dbusInterface.PressedPause()
    
    def stop(self):
        self.__dbusInterface.PressedStop()
    
    def next(self):
        self.__dbusInterface.PressedNext()
    
    def previous(self):
        self.__dbusInterface.PressedPrevious()


if __name__ == '__main__':
    parser = OptionParser(usage='usage: %prog [options] ', version=Version, description="Multimedia Key Daemon")  
    parser.add_option('-p', '--play', action='store_true', help='send play event to all listeners', dest='play', default=False)
    parser.add_option('-a', '--pause', action='store_true', help='send pause event to all listeners', dest='pause', default=False)
    parser.add_option('-s', '--stop', action='store_true', help='send stop event to all listeners', dest='stop', default=False)
    parser.add_option('-n', '--next', action='store_true', help='send next-track event to all listeners', dest='next', default=False)
    parser.add_option('-b', '--previous', action='store_true', help='send previous-track event to all listeners', dest='previous', default=False)
    parser.add_option('-d', '--daemon', action='store_true', help='start the daemon, if not already running', dest='daemon', default=False)
    (options, args) = parser.parse_args()
   
    if args=="none":
        parser.print_help()
    
    if options.daemon:
        d = Server()
    else:
        if options.play:
            client = Client()
            client.play()
        elif options.pause:
            client = Client()
            client.pause()
        elif options.stop:
            client = Client()
            client.stop()
        elif options.next:
            client = Client()
            client.next()
        elif options.previous:
            client = Client()
            client.previous()
        else:
            parser.print_help()
