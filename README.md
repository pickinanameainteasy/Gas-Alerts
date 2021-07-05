# Gas-Alerts
This tool sends alerts to your device when ETH gas prices are less than are equal to a user specified price.

# How to get started
Run install_modules.bat (Windows) or install_modules.sh (Linux). NOTE: you must have both python and pip install for these files to work.

Alternatively, you can install requests-html and notify-run using the following commands:

pip install requests-html

pip install notify-run

Once these modules are installed you must run either setup_notify_run.bat (Windows) or setup_notify_run.sh (Linux). You will be presented with a URL and a QR code (the QR code may not display correctly). Visit this URL or scan the QR code on the device you wish to receive notifications on. On the website that opens click the blue button that says "Subscribe on this device." Make sure the button turns gray and says "Already Subscribed." 

You may also add additional devices by visisting the same URL or scanning the QR code listed on the webpage and pressing "Subscribe on this device" on that device.

Once you are subscribed you may close the webpage. You may visit the URL to unsubscribe.

# Configuring the script
Once the notifications are set up you may open the Gas_Alerts.py file. Here you should locate the line that reads "limit = 15." This determines at which price the script will notify you. You may change this value to any number and the script will send you a notification when the fast gas price is less than or equal to this value.

The limit variable is tied to the 'fast' price on https://gasnow.org/, future updates may allow users to choose between 'rapid,' 'fast,' 'standard,' and 'slow.'

After setting the limit, scroll down to the line that reads "notify.send('')." Here you should type the message you want to appear in the notification between the two quote marks.

Once both the limit and the notification are set you may close the Gas_Alerts.py file.

# Running the script
This script works best when set to run periodically either by using Task Scheduler (Windows) or crontab (Linux).

# Issues
The install_modules.sh and setup_notify_run.sh scripts may not work correctly, for now Linux users may be required to manually install the two modules.
