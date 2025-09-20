# 100-Youtube-Auto-Likes-Using-Localhost

100+ Youtube Non Stop Auto Likes For Videos and shorts Using selenium with python on localhost

# For Shorts:-

https://github.com/yashu1wwww/100-Youtube-Auto-Likes-For-Youtube-Shorts-Using-Localhost

## "If you know proxy rotation, then please fork it".

https://www.youtube.com/watch?v=FVumnHy5Tzo&t=1s&ab_channel=HelloWorld

## Watch up to 3 minutes and 46 seconds, and then remain in the remaining part copying the part of the script and save it as l.py. 

The script is used to automatically like a particular YouTube video with multiple accounts

First, open Chrome file location and bypass the location restriction using an extension such as Touch VPN. In my case, the Chrome location(use start in: path) is

## C:\Users\Hp\AppData\Local\Google\Chrome\Application

click window button and search cmd and enter

cd 

## C:\Users\Hp\AppData\Local\Google\Chrome\Application (1st line in cmd)

in line enter

## chrome.exe --remote-debugging-port=9222 --user-data-dir=""(in "enter your localhost path here")

Next, enter this command into the terminal, replacing "enter your localhost path here" with your localhost path:

For example, in my case it is:

## chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\Users\Hp\Desktop\Bots\Chromedriver\Localhost" (2nd line in cmd make sure you replace the localhost path)

# then again open new terminal in that folder enter

pip install selenium==4.2.0

after enter l.py or double click on l.py

This will open the YouTube video URL in Chrome, automatically like it with multiple accounts, and switch between accounts to hit the likes.

# "You must login with your 10+ accounts,

# after login with 10 accs add these extension
https://shorturl.at/mtAER

and each account must have 10+ brand accounts to hit auto-likes. In the 15th line of the script, replace the URL with the YouTube video URL you want to like.

That's it! The URL will open in the previously opened localhost Chrome and 100+ auto likes will be done automatically.

--------------------------------------------------------------------------------------------------------------------

# 👉 Note:Every time YouTube updates its code, it may vary. So, open the YouTube video, press *Ctrl + Shift + C* to open Developer Tools, inspect the elements, find the updated paths, and modify accordingly. 

---------------------------------------------------------------------------------------------------------------

# 👉Note:-

👉If you have the latest version of Selenium, the code may not run

👉open cmd and enter pip uninstall selenium

And enter

pip install selenium==4.2.0

and hit enter

and

python -c "import selenium; print(selenium.version)"

𝙏𝙝𝙞𝙨 𝙞𝙣𝙛𝙤𝙧𝙢𝙖𝙩𝙞𝙤𝙣 𝙞𝙨 𝙤𝙣𝙡𝙮 𝙛𝙤𝙧 𝙚𝙙𝙪𝙘𝙖𝙩𝙞𝙤𝙣al 𝙥𝙪𝙧𝙥𝙤𝙨𝙚 𝙖𝙣𝙙 𝙬𝙚 𝙖𝙧𝙚 𝙣𝙤𝙩 𝙧𝙚𝙨𝙥𝙤𝙣𝙨𝙞𝙗𝙡𝙚 𝙛𝙤𝙧 𝙖𝙣𝙮 𝙠𝙞𝙣𝙙 𝙤𝙛 𝙞𝙡𝙡𝙚𝙜𝙖𝙡 𝙖𝙘𝙩𝙞𝙫𝙞𝙩𝙮 𝙙𝙤𝙣𝙚 𝙗𝙮 𝙩𝙝𝙞𝙨 𝙩𝙤𝙤𝙡.
