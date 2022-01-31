# Product management

## Description: 
- The product can have the following fields
Name, product code, price, category, manufacture date, expiry date, owner, status
Include Basic user registration and login functionality
- Category can be a subcategory of other categories & possibly N number of depth.
- Create a basic UI for super user to perform CRUD on Product- with search and filter by category or any
other product attribute
- Create a basic UI for super user to perform CRUD for Category- with search and filter category name
and
- Create Basic UI to list out all the Products and Categories for end-user (Separate Menus for Product
and Category)
> The only owner of the product can update/delete the product if other users tries update show
proper message
> Owners can only change the price of the product once per day before 11:00 AM (show proper
validation message)
> Price change must be in the range -10% to + 10% (I.e price of the product is 100 then oiler can
set to min 90 and max 110)
> Admin should be able to know when the product is created and when it is updated (date and
time) - only for Django admin panel
> In the admin Panel add a filter and search with all details in the display
- You have to use Django rest framework for writing API for Category and Product both (send postman
collection link)
- Write Basic cron that will delete the expired product everyday 00:00:00 IST.
- Update the code with proper requirement’s and README file to Github/bitbucket and share the link


### Follow the below steps to setup the project:

**Step 1: Create python3 virtual environment and activate it:**
```
virtualenv -p python3.6 venv
source venv/bin/activate
```

**Step 2: clone the repo and checkout to the master branch**
```
git clone https://github.com/khushu729/product_management.git
git checkout master
```

**Step 3: Install the requirments**
`pip3 install -r requirements.txt`

**Step 4: Migrate the database**
`python3 manage.py migrate`

**Step 5: Run the server**
`python3 manage.py runserver`

**Step 6 (optional): load the given data**
`python3 manage.py loaddata  db.json`

**Step 7 : you can use the below superuser login credential to test the flow**
```
username: khushbu
email: khushbu@gmail.com
password: 1234
```

## Use the below commands to run the cron job. 
`python manage.py crontab add`  # this will add the crontab which is listed in the settings file
`python manage.py crontab remove`
`python manage.py crontab show`

**Demo link:** https://www.loom.com/share/0c93eae098b64bb8ae6c818327346dcd

## You can check the api document using below urls:
http://localhost:8000/redoc/
http://localhost:8000/doc/