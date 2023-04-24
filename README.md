**Project Structure**

- In this project, I use somewhat MVC (Model, View, Controller) pattern and I use Motor driver for MongoDB operations.
- Here I use Routers, Service and Core for design pattern.

  - **Routers** :- 
    - It is the starting point of each and every API request. Here I declare HTTP method, Request Body (if any), Query parameter (if any) as Response of APIs.
    - For example :-  In user router, all respective apis are there for creating user, searching users and fetch any single user.
    
  - **Service** :-

    - Service is the middle layer of API request processing which contains business logics.
    - E.g. :-  Converting commands into Models, Response conversion to state format, validations etc.  
  
  - **Core** :-
    
    - It is the last layer which directly connects with database, do operations and returning database objects to service layer.
    - E.g. :-  Save model, Fetch particular model object, Searching objects with pagination and many more.
   


---

## Features

- Here I list out some of additional features which are useful in real world.

  1. **Logger** :- It is used for monitoring and troubleshooting.
  2. **Environment Variables** :- In real time, environment variables are used to secure sensitive parameters like Database Host, Port, Name etc.
  3. **Swagger** :- Documentation of API is a needy thing nowadays. It makes API integration very easy for Frontend developer as well third party clients to integrate in their system. Swagger is one of the most popular OpenAPI documentation format.

---

## List of APIs

- User APIs
  
  - Create a user :-  (POST) http://127.0.0.1:8000/cosmocloud/v1/user
  - Search users with pagination :-  (POST)  http://127.0.0.1:8000/cosmocloud/v1/user/search
  - Fetch a single user :-  (GET) http://127.0.0.1:8000/cosmocloud/v1/user/{user_id}

- Organisation APIs

  - Create an organisation :- (POST) http://127.0.0.1:8000/cosmocloud/v1/organisation
  - Search organisations with pagination :-  (POST) http://127.0.0.1:8000/cosmocloud/v1/organisation/search

- Permissions APIs

  - Create permission :-  (POST) http://127.0.0.1:8000/cosmocloud/v1/permission
  - Update permission by id :- (PUT) http://127.0.0.1:8000/cosmocloud/v1/permission/update/{permission_id}
  - Update permission by user id & org id :- (PUT) http://127.0.0.1:8000/cosmocloud/v1/permission/update/organisation/{org_id}/user/{user_id}
  - Remove Permission by id :- (DELETE) http://127.0.0.1:8000/cosmocloud/v1/permission/{permission_id}
  - Remove Permission by user id & org id :- (DELETE) http://127.0.0.1:8000/cosmocloud/v1/permission/organisation/{org_id}/user/{user_id}

---

## DB Setup

1. Create MongoDB with name :- ``cosmocloud_db`` & also add one collection ``users``
2. Create user for it :- user = ``testUser``, password = ``admin``
3. If you want to use other user and password then please change them into ``.env`` file.


---

## Note

- Please use following values for permission type.
    
  - For READ type, Use ``0`` in command
  - For WRITE type, Use ``1`` in command
  - For ADMIN type, Use ``2`` in command