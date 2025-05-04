# Finances API

A locally hosted finances-oriented API developed to be consumed from whatever app you'd like to build.

You can use `C++ with Qt`, `Python with TKinter`, `NodeJS with Angular` or any other UI developing library/framework you preffer.

---

## Deploy

To host and deploy the API, run `python manage.py runserver`.

## Endpoints

Once hosted, you can access the endpoints from the base [URL](http://localhost:8000/).

Take a look to the [auto-generated docs](http://localhost:8000/docs) to get some more info about the available endpoints.

## Build

This project was originally meant to be ran and accessed locally, hosted from an executable file.

You can build the executable by running `pyinstaller manage.py --name server --noconfirm` or executing the [build.bat](/build.bat) script from the terminal. After the building process, you'll end up with 2 folders, the final product is located at `/dist`.

## Storage

All the data is located at the [db.sqlite3](/db.sqlite3) file, in case you need to rebuild the server just save a copy of that file.

> ⚠️ If you modify the model structures (any of the `models.py` files), your saved data could be lost **completely**.