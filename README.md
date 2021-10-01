## Clone for ecommerce app - jiji

'ecommerce' is a django app designed to provide a medium of communication between buyers and sellers.

## Database 

*sqlite*

## Role Based Access Control

##### Buyers are allowed to:
- view all available products
- indicate interest in a product by providing necessary details
- Communicate with the seller via the details provided


##### When a Seller logs in, he should be able to:
- view all his products
- add new product by providing the necessary data fields for that product
- edit a product
- get request from buyers
- delete product

## API structure

### Base URL
This url for the app is https://ecommerce-backend-app1.herokuapp.com/



##Installing Dependencies

#### Python 3.7

As provided here, install the latest version of python [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)


#### Establish a virtual Enviornment

Virtual environments provide a decent level of modularity for projects making a developer able to distinguish one project from another.
It also houses the dependencies for the project. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Install dependencies via the provided `requirements.txt` file

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.


### Error Handling
Errors are returned in JSON format, objects with "success" set to False, "error" set to the error code along with 
the corresponding error message.

Possible errors:
- 400: Bad Request
- 403: Forbidden
- 404: Resource Not Found
- 422: Request can not be processed
- 500: Internal Server Error

### *Endpoints*

Asides the `get` request, every other request requires *authentication*


##### GET  '/api/products'
    This endpoint retrieves all the products in the database and displays them as json.


##### POST '/api/products'
    This endpoint creates a new product in the database based on the data provided. 


##### PATCH  '/products/<int:note_id>'
    This endpoint will modify the product that corresponds to the query parameter note_id that is passed into the url.


##### DELETE  '/api/products/int:<note_id>'
    This endpoint will delete the product that corresponds to the ID that is passed into the url.


##### GET  '/api/buyers'
    This endpoint fetches all the buyers in the database and displays them as json.


##### POST '/api/buyers'
    This endpoint will create a new buyer resquest in the database based on the json that is in the body of the request.

##### PATCH  '/buyers/<int:note_id>'
    This endpoint will modify the product that corresponds to the note ID that is passed into the url based on the json that is passed into the body of the request.


##### DELETE  '/api/buyers/int:<note_id>'
    This endpoint will delete the buyer that corresponds to the note ID that is passed into the url.

##### GET  '/api/users'
    This endpoint fetches all the users in the database and displays them as json.


##### POST '/api/users'
    This endpoint will create a new user in the database based on the json that is in the body of the request.

##### PATCH  '/users/<int:note_id>'
    This endpoint will modify the user that corresponds to the note ID that is passed into the url based on the json that is passed into the body of the request.


##### DELETE  '/api/users/int:<note_id>'
    This endpoint will delete the user that corresponds to the note ID that is passed into the url.

## Running the server


To run the server, execute:

```
python manage.py runserver
```

