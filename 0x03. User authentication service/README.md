# 0x03. User authentication service

## In this project

- you will implement a User authentication service. You are not allowed to implement any other services. This service will be consumed by other services (yourself and other engineers) so it is important that you keep your codebase as simple and as clean as possible. If you notice that you are adding too much “features” to your API, you are probably doing something wrong. For example, you should not try to implement permissions or validations within the API. These kind of constraints should be implemented in the client side. The API is only there to “serve” data, not to validate it. Having a simple API will also help you with the upcoming project: “Simple API”. The authentication system will provide a token to consumers. A token can be for example an JWT or a session key. If you are curious on how to implement a session key, check this article. For this project, you will store all documents in a MongoDB database. MongoDB provides official clients for most popular languages. You should use these clients. You should not use any ODM (Object Document Mapper) as this is considered an anti-pattern. If you want to use an ODM because you think it will help you to write less code, you are probably doing something wrong. You may also want to read about common anti-patterns when using MongoDB

## Resources

### Read or watch

- Authentication Cheat Sheet | OWASP - The Open Web Application Security Project
- Authentication | MDN
- Cookies and Sessions | YouTube
- Session Hijacking | YouTube
- JWT Crash Course | YouTube
- Cookies vs Tokens. Getting auth right with Angular.JS | YouTube
- CSRF Attacks | YouTube
- Same Origin Policy (SOP) | YouTube
- Cross-Origin Resource Sharing (CORS) | YouTube
- CORS | MDN
- OWASP Top 10 2017: Broken Authentication | YouTube
- Flask Cookies
- Flask Sessions
- Flask SQLAlchemy
- Flask Tutorial #7 - User Authentication and Login
- Flask-Bcrypt
- Flask-JWT-Extended
- Flask-Login
- Flask-Principal
- Flask-WTF
- Flask-CORS
- Flask documentation
- Flask SQLAlchemy documentation
- MongoDB Extended JSON
- MongoDB C Driver
- Mongo Procotol, Message Header, OP_QUERY, OP_REPLY
- MongoDB: Aggregation
- MongoDB: How to Create Indexes to Optimize Queries
- MongoDB: Data Modeling
- MongoDB: Introduction to Indexes
- MongoDB: Compound Indexes
- MongoDB: Aggregation Pipeline
- MongoDB: How to Perform Aggregation with Group in MongoDB
- MongoDB: Aggregation Pipeline
- MongoDB Indexing Strategies and Aggreation

- Context
- What is an API? What is a token?
- What is an API token?
- What is the difference between authentication and authorization?
- What is a session?
- What is a session cookie?
- How to map a JWT to a session cookie?
- What are the benefits of using JWTs over session cookies?
- What are the benefits of using session cookies over JWTs?
- How to generate an access token?
- How to get an access token from a cookie?
- How to generate a refresh token?
- How to get a refresh token from a cookie?
- How to access a protected resource?
- What is HTTPS?
- For what is used HTTPS?
- What are the steps in the JWT authentication process?
- What are the steps in the secured API authentication process?
- How to implement authentication with a database?
- How to implement authentication with a database and a cache?
- How to deploy a simple API?
- How to handle pagination with a simple API?
- How to handle authentication pagination?
- How to communicate with a third party service that is not connected to your database?
- How to write docstrings for API routes?
- How to write an API documentation?
- How to write documentation for each module and function?
- What are the limits of API documentation?
- How to make your API more discoverable through API pagination?
- How to paginate a large dataset with MongoDB?
- How to paginate a large dataset with Redis and Flask?
- How to paginate a large dataset with SQLAlchemy?
- How to paginate a large dataset with SQLAlchemy and Flask?
- How to paginate a large dataset with SQLAlchemy and Redis?
- How to paginate a large dataset with SQLAlchemy and Redis and Flask?
- How to paginate a large dataset with SQLAlchemy and Redis and Flask and cache key?
- How to paginate a large dataset with SQLAlchemy and Redis and Flask and cache key and cache timeout?

## Learning Objectives

### At the end of this project, you are expected to be able to explain to anyone, without the help of Google

- How to declare API routes in a Flask app
- How to get and set cookies
- How to retrieve request form data
- How to return various HTTP status codes
- How to return JSON format the easy way
- How to retrieve request arguments
- How to create a MySQL database
- How to declare MySQL User-Access privileges
- How to connect to a MySQL database from a Flask app
- How to SELECT data from a MySQL table in a Flask app
- How to INSERT data into a MySQL table in a Flask app
- How to UPDATE data in a MySQL table in a Flask app
- How to DELETE data from a MySQL table in a Flask app
- How to create a MySQL table with SQLAlchemy
- How to handle SQLAlchemy warnings
- How to filter data from a MySQL table with a WHERE
- How to handle pagination with SQLAlchemy

## Tasks
