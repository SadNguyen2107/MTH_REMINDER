import os 
import winshell
from win32com.client import Dispatch

def validateShortcutPath():
    desktop = winshell.desktop()
    file_path = os.path.join(desktop, 'MTH1125_Announcement.lnk')

    if not os.path.exists(file_path):
        answer = input('Do you wish to create a shortcut on your Desktop? [Y] or [N]: ').lower()
        
        if answer == 'y':
            return True
            
        elif answer == 'yes':
            return True

    return False
    
def createShortcut():
    if validateShortcutPath():
    
        # Path to the desktop folder
        desktop = winshell.desktop()

        # Create a shortcut to your desktop computer
        path = os.path.join(desktop, 'MTH1125_Announcement.lnk')

        # Define the target file path, working directory path, and icon path for shortcut
        target = os.path.join(os.getcwd(), 'MTH_Reminder.exe')
        wDir = os.getcwd()

        # Create a new instance of the Windows Script Host Shell object 
        # and use it to create a new shortcut object.
        shell = Dispatch('WScript.Shell')
        shortcut = shell.CreateShortCut(path)

        # These lines set the properties of your shortcut object 
        # (target path, working directory, and icon location) and save it to disk.
        shortcut.Targetpath = target
        shortcut.WorkingDirectory = wDir
        shortcut.save()