from __future__ import print_function
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
from requests import get
from xml.etree import ElementTree
from yagmail import SMTP
import os

items_wanted = {
    "Outdoor sectional": "S59028752"
}
local_stores = {
    "PA, Conshohocken": 211,
    "PA, South Philadelphia": 215,
    "NJ, Elizabeth": 154,
    "MD, Baltimore": 152
}
region = 'us'
locale = 'en'
availability_url = 'http://www.ikea.com/{region}/{locale}/iows/catalog/availability/{item_id}'


def query():
    available = False
    output = []
    gmail_user = os.environ.get('GMAIL_USER')
    gmail_password = os.environ.get('GMAIL_PASSWORD')

    for item_name, item_id in items_wanted.items():
        availability_data = get(availability_url.format(region=region, locale=locale,
                                                        item_id=item_id))

        for city, code in local_stores.items():
            available_qty = int(ElementTree.fromstring(availability_data.content)
                                .find(".//localStore[@buCode='{code}']".format(code=code))
                                .find('.//availableStock').text)
            if available_qty > 0:
                available = True
                message = "{} available {} ({}) {} @ {}".format(
                    available_qty, item_name, item_id, city, datetime.now())
                output.append(message)
                print(message)

    if available and gmail_user and gmail_password:
        SMTP(gmail_user, gmail_password).send(to=gmail_user, subject='Ikea Availability',
                                              contents='\n'.join(output))
    else:
        print('No items available @ {}'.format(datetime.now()))


if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_job(query, 'interval', hours=1)
    print('Press Ctrl+{} to exit'.format('Break' if os.name == 'nt' else 'C'))

    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        print('See ya!')

