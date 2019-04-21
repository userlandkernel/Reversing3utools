# Reverse engineering 3utools tutorial

## Requirements
- Microsoft windows 7 or higher, possibly a virtual machine.
- Telerik's Fiddler (or burpsuite) (https://www.telerik.com/fiddler)
- 3utools desktop application (3utools.com)
- Dirbuster

## Preparations
- Install 3utools.
- Install Telerik's Fiddler (or burpsuite)
- Close 3utools if open, in the tray as well.
- Launch Fiddler and enable the proxy, default it is running on port 8888.
- Launch 3utools and press the settings icon on the top right.
- Now click proxy settings and enter localhost with the port from fiddler.

## Reversing 3utools
1. In fiddler you can now click the hitmark icon, drag it onto 3utools and turn decode on.  
2. You will now be able to see the SSL traffic of 3utools through fiddler.  
3. Any operation that is done by communicating through their api like for example a search query will appear in fiddler.  
4. One can click the requrest and choose raw to see what the 3utools api responded to the application.  
