#Ikea Stock Checker

Python script for notifying you when items become in stock. It can check multiple items on multiple stores.

**Note:** Gmail account required for email notification


###Installation

1. cd to directory where this code is cloned.
2. *optional* - create new virtual env
3. Install requirements

        pip install -r requirements.txt

4. *optional* - create environment variables if you want to be notified via email

        export GMAIL_USER=user.name@gmail.com
        export GMAIL_PASSWORD=mySecretPassword

5. modify `items_wanted` variable with your item(s) you want to check for availability. This value can be found in the URL. Ex: when I wrote this, I was looking for: http://www.ikea.com/us/en/catalog/products/S59028752/ so the value you need from the URL is: `S59028752`

        items_wanted = {
           "any arbitrary name you want to use": "S59028752"
        }

6. modify `local_stores`. For this you'll have to do some digging in the HTML itself to find all the dropdown values that correspond with the stores you want to use.

        local_stores = {
            "PA, Conshohocken": 211,
            "S Philly": 215,
            "Whatever name you want to use": 154,
            "MD, Baltimore": 152
        }

7. *optional* - modify local. If you are in the USA you do not need to do anything. If you are located elsewhere than you need to modify `region` and `locale` variables. These values are in the URL.
8. Done. Run it via: `python ikea-stock-checker.py` or `python3 ikea-stock-checker.py`
