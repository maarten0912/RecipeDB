# Recipe database
 - Use the `bbc-downloader.sh` script to download all (10171)  recipes from https://www.bbc.co.uk/food. This will probably take more than 30 minutes, depending on your internet speed. If you don't want to do that and just need to test, you can use the `small` folder which has only 240 recipes.
  - (Optional:) Create a virtual environment if you don't want to install pip modules on your machine directly.
    - `$ python -m venv venv` to make a virtual environment.
    -  `$ source venv/bin/activate` to use the virtual environment. On windows you can probably use `venv/bin/Activate.ps1` or someting but I don't know how to do that.
  - Install necessary pip modules: `$ pip install pyquery tqdm`
  - Run `$ python init.py` to initialize the database
  - Run `$ python script.py <recipefolder>` to populate this database with the data
  - Run `$ python init2.py` to initialize the full text search database (this needs to be done after populating the database)
  - Run `$ python script2.py` to search the database