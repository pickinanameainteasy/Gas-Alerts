from requests_html import HTMLSession
from notify_run import Notify

# get webpage
session = HTMLSession()
r = session.get('https://gasnow.org')
r.html.render(sleep=5)

# gas price to be alerted at
limit = 15		# CHOOSE THE VALUE YOU WANT TO BE ALERTED AT

# set notification
notify = Notify()

# find gas price
elements = r.html.xpath('//strong')

# decide if gas is low
if int(elements[2].text) < limit:
    print('cheap gas')
    notify.send('')	# TYPE NOTIFICATION BETWEEN THE QUOTES
else:
    print('expensive gas.')
