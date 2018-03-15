Title: Accessing wired Windows printer from your Mac
Date: 2015-12-20 12:52
Modified: 2018-03-15 15:46
Status: published
Category: Hardware hacks
Tags: hardware, mac
Slug: Accessing_wired_Windows_printer_from_your_Mac
Authors: Al Krinker
Summary: What to do when you are faced with 'Please, commit your changes or stash them before you can merge.' message from git as you are trying to get latest code off your remote repository

Before my PC seized to be, I used to have old wired printer that did the job... the only problem was that I already have few Apple laptops and I wanted to be able to print from them (The problem is easily solved by buying wireless printer that supports AirPrint, i.e. even print from your iPhone!).

Anyway, if you have wired Windows printer and don't want to upgrade just yet here is what you need to do:

On Windows PC<br />
1. Establish user account on your PC. This was one thing that I had to do to make everything that should work to actually work. This is as easy as opening your control panel and clicking on Add user in your Users menu. For more tricks see this: http://www.howtogeek.com/howto/10325/manage-user-accounts-in-windows-home-server/<br />
2. Now onto actual set up... Select Start->Devices and Printers. Right click on the printer that you want to share, and either pick share or properties and then pick sharing tab. Make sure that share check box is selected and make sure that you note down the name of the printer.<br />
3. Open command prompt. Use ipconfig command to find your PC's IP.<br />

To summarize this part. You have IP address and name of the printer to connect to and you have the credentials that you created in step 1.

On MAC<br />
1. Open System Preferences and locate Printers and Scanners icon. Click!<br />
2. Select + under printers to add new printer, i.e. wired Windows printer.<br />
3. Right click on the menu and select Customize Toolbar and add Advanced<br />
4. Click on Advanced. For type select Windows printer via spoolss<br />
5. For URL provide IP and printer name that you have... so the link looks like smb://192.138.1.13/printer_name (Replace any spaces with %20 in your<br />
6. Under Choose a driver or Printer Model pick your printer type (I did not see my exact model so I picked closes HP model instead. Worked)<br />
7. At this point your PC printer will be connected to your Mac.<br />

Testing<br />
Select something to print on your Mac... in my case, the first time it tried to print it asked for my PC username/password which we created previously, after that it was stored in my keychain and was never an issue again.

That's it! Hope it helps and once again, let me know if you have further questions, etc.
