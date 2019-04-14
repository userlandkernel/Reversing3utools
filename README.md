# Reversing3utools
Reverse engineering the commonly used 3utools software to make it more open and learn about it.  

## Why
3utools is amazingly great software for managing iOS devices.  
Not only does it show you a lot information about hardware integrity of your devices, it also helps you fix problems and jailbreak them.  
3utools is not opensource but has an API for most of their functionality.  
For the freedom of development I wanted to see if this API can be reused by developers as that would make the life of security researchers easier.  

## The Research
3utools has the ability to specify a proxy in the settings.  
Since the traffic of 3utools is encrypted via TLS, I am using fiddler with its own CA certificate.  
After launching fiddler I simply set the proxy server in the settings to be localhost with port 8888, which is what fiddler runs on.  
Burpsuite is also possible the same way which is amazing for debugging API calls and reproducing / interacting with API calls.  

## First 0-day vulnerability reported

Without even using any research tools like burpsuite and fiddler I expected that most of the content loaded in 3utools is actually just a webpage with a lot of javascript, this due to the delays in rendering certain userinterface graphics because that could mean and turned out to be loaded over the network.  

3utools was vulnerable to a low-risk cross site scripting vulnerability which I found by simply entering "<script>alert(1)</script>" in almost any of the input fields a user could access in the software. 
With that I also found the domain where their UI is located at.  

Without further interruption or waiting, I immediately reported the vulnerability to 3utools and it got patched the same day.  
However, I did not get any bounty. After all 3utools is free software anyway.  

## Amazing infrastructure
3utools seems to have amazing infrastructure.  
They have a persitant file storage server where they store almost any iOS firmware related files, such as developer dmgs and jailbreaks.  
This makes their service faster than Apple's and able to download files even when Apple's servers are down.  
What is where and where is what is yet to be found out, but at least I discovered that when clicking the 'view screen' button you can see that the corresponding developer dmg image is downloaded for your device and mounted.  
Probably because they use the 'screenshotr' xpc service to get the live screen.  
For developers and researchers this means it is amazingly easy to quickly download the developer dmg from their servers as they are all named logically.  

Aside the filestorage they also have a REST json API with one can retrieve information about firmware.  
One can ask the API to only give jailbreakable or jailbreakable and signed firmware or just any firmware for specific devices and OS versions.  
Great feature if you ask me, again for developers and researchers a good way to automate their work a few more.  
