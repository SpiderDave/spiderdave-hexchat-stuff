__module_name__ = "OpenLogFile"
__module_version__ = "1.0"
__module_description__ = "Adds a context menu item to open log files/folder"
__author__ = "SpiderDave"

import xchat
import hexchat
import os

def cmd(stuff):
    xchat.command(stuff)

    def menu_clear(self):
        menu_del("Overwatch/"+self.name)

def menu_add(path, command=None, pos=None):
    if command:
        body = '"{}" "{}"'.format(path, command)
    else:
        body = '"{}"'.format(path)
    if pos:
        cmd("MENU -p{} ADD {}".format(pos, body))
    else:
        cmd("MENU ADD "+body)

def menu_item(path, command=None, network="", channel=""):
    path = '"Window/logs/'+path+'"'
    if command:
        path += ' "'+command+'"'
    cmd("MENU ADD "+path.format(name='Window/logs', net=network, chan=channel))

def menu_del(path):
    cmd('MENU DEL "{}"'.format(path))

def menu_clear():
    menu_del("Window/logs")

def unload_openLogFolder(userdata):
    pass

def unload_openLogFile(userdata):
    pass

def openLogFolder(word, word_eol, userdata):
    if len(word)>1:
        hexchat.command('help openLogFolder')
    else:
        path = hexchat.get_info('configdir')
        logFile = '%s%slogs' % (path, os.sep)
        os.startfile(logFile)
    return hexchat.EAT_ALL

def openLogFile(word, word_eol, userdata):
    if len(word)>1:
        hexchat.command('help openLogFile')
    else:
        path = hexchat.get_info('configdir')
        logFile = '%s%slogs%s%s%s%s.log' % (path, os.sep, os.sep, hexchat.get_info('host'),os.sep, hexchat.get_info('channel'))
        os.startfile(logFile)
    return hexchat.EAT_ALL

def load(*args):
    hexchat.hook_command('openLogFile', openLogFile, help='openLogFile')
    hexchat.hook_command('openLogFolder', openLogFolder, help='openLogFolder')
    hexchat.hook_unload(unload_openLogFile)
    hexchat.hook_unload(unload_openLogFolder)
    menu_clear()
    menu_add("Window/logs")
    menu_item("open log file", "openLogFile")
    menu_item("open logs folder", "openLogFile")
    hexchat.prnt("Loaded.")

def unload(*args):
    pass

# Defer load until config files stabilize
xchat.hook_timer(100, load)
xchat.hook_unload(unload)