# 100-Youtube-Auto-Likes-Using-Localhost

100+ Youtube Non Stop Auto Likes Using selenium with python on localhost

## Couldn't find it on Google, so I created it.

𝙉𝙤𝙩𝙚:𝘿𝙞𝙙𝙣'𝙩 𝙘𝙤𝙥𝙮-𝙥𝙖𝙨𝙩𝙚 𝙘𝙤𝙙𝙚 𝙖𝙜𝙖𝙞𝙣 𝙖𝙣𝙙 𝙖𝙜𝙖𝙞𝙣 𝙎𝙤𝙢𝙚 𝘾𝙝𝙖𝙣𝙜𝙚𝙨 𝘼𝙧𝙚 𝙏𝙝𝙚𝙧𝙚.

## "If you know proxy rotation, then please fork it".

## in lc.py script

https://www.youtube.com/watch?v=FVumnHy5Tzo&t=1s&ab_channel=HelloWorld

## Watch up to 3 minutes and 46 seconds, and then remain in the remaining part copying the part of the script and save it as l.py. 

The script is used to automatically like a particular YouTube video with multiple accounts

First, open Chrome file location and bypass the location restriction using an extension such as Touch VPN. In my case, the Chrome location(use start in: path)  is

C:\Users\Hp\AppData\Local\Google\Chrome\Application

Next, in the command prompt, navigate to the Chrome directory using the command cd C:\Users\Hp\AppData\Local\Google\Chrome\Application

Then, 

use the command

chrome.exe --remote-debugging-port=9222 --user-data-dir="enter your localhost path here" 
  
to open Chrome with remote debugging enabled. In my case, the command was
  
chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\Users\Hp\Desktop\Bots\Chromedriver\Localhost" 

then new terminal in that folder and enter l.py (letter l not one)

After opening Chrome, paste the following two lines of code from the script into the command prompt and hit enter. 

This will open the YouTube video URL in Chrome, automatically like it with multiple accounts, and switch between accounts to hit the likes.

# "You must login with your 10+ accounts,

# after login with 10 accs add these extension
https://shorturl.at/mtAER

and each account must have 10+ brand accounts to hit auto-likes. In the 17th line of the script, replace the URL with the YouTube video URL you want to like.

That's it! The URL will open in the previously opened localhost Chrome and 100+ auto likes will be done automatically.

Finally, in the command prompt, enter "pip install Random" and hit enter to install the necessary library.

## 👉 Note:Every time YouTube updates the code, it varies. So, open the YouTube video, press 'Ctrl+Shift+C' to open the developer tools,

## then copy the 'Like' button's XPath, CSS, or JavaScript path. Replace it in the code and press 'Ctrl+H' to find and replace the same element in the code.

--------------------------------------------------------------------------------------------------------------------

## 👉 "If you want 1000 auto likes, follow these steps in Chrome settings:

Click on the account logo near the top
Go to 'Other profiles.'
Click the '+ Add' button.
Log in with 10 different Gmail accounts, with each Gmail account containing 10 brand accounts.
Repeat this process for a total of 8 profiles, with each profile containing 10 emails (each email having 10 brand accounts).

## Once you've set up the profiles, open each one and double-click on the Python (L.py) file. That's it!"

-----------------------------------------------------------------------------------------------------------------------

## For Creating Gmail Without Phone And Create Within 1 Minutes Use These 👇

## Mobile Settings > Password & Accounts > Google > Choose to create an account at the bottom. When prompted, select "Myself," fill in the remaining details, and note that they won't ask for a phone number.

## You can try these steps to create a Gmail account without providing a phone number.

-------------------------------------------------------------------------------------------------------------------------

👉Note:-

👉If you have the latest version of Selenium, the code may not run

👉open cmd and enter pip uninstall selenium

And enter

pip install selenium==4.2.0

and hit enter

and

python -c "import selenium; print(selenium.version)"

𝙏𝙝𝙞𝙨 𝙞𝙣𝙛𝙤𝙧𝙢𝙖𝙩𝙞𝙤𝙣 𝙞𝙨 𝙤𝙣𝙡𝙮 𝙛𝙤𝙧 𝙚𝙙𝙪𝙘𝙖𝙩𝙞𝙤𝙣al 𝙥𝙪𝙧𝙥𝙤𝙨𝙚 𝙖𝙣𝙙 𝙬𝙚 𝙖𝙧𝙚 𝙣𝙤𝙩 𝙧𝙚𝙨𝙥𝙤𝙣𝙨𝙞𝙗𝙡𝙚 𝙛𝙤𝙧 𝙖𝙣𝙮 𝙠𝙞𝙣𝙙 𝙤𝙛 𝙞𝙡𝙡𝙚𝙜𝙖𝙡 𝙖𝙘𝙩𝙞𝙫𝙞𝙩𝙮 𝙙𝙤𝙣𝙚 𝙗𝙮 𝙩𝙝𝙞𝙨 𝙩𝙤𝙤𝙡.
