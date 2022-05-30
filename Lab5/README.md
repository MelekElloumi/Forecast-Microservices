# Software architecture lab 4: Loan management
This is lab 5 of [software architecture lab](https://insatunisia.github.io/TP-ArchLog/tp5/)
- work by Melek Elloumi

## Application description
- The objective of this lab is to define the architecture and develop a demo of a backend of an online shopping
web application that lets clients buy products and lets warehouses manage inventory. 
- Clients can also subscribe to products and wait for a notification for when they come back in stock.
- It's basically a CRUD on products divided between clients and warehouses.

## Architecture

### Hybrid architecture

- The backend interacts with both clients and warehouses based on the shared products' database.
- From the client side, it should be able to view and buy products through the api.
- From the warehouse side, it should be able to view,add,delete the products through the api.
- The database needs to be consistent and synchronised between the two.
- In order to solve this, we need a hybrid architecture that mix between an architecture that realise the main functionalities and an architecture that 
favors this type of communication.
- GLx found that a microservice architecture and a CQRS architecture would be a good solution.
- We divided ourselves into 2 teams, one for realising microservice, the other for CQRS, and we assigned a leader
between them to assure that our work is well-coordinated.

### Microservices

- The backend logic that process products queries are deployed in microservices that expose an api for clients and warehouses
to use.
- This solution is maintainable and scalable.
- It uses CQRS services to access the database.

### CQRS
- The Command and Query Responsibility Segregation (CQRS) is an architectural pattern where the main focus is 
to separate the way of reading and writing data.
- This will ensure that products' data is consistent when reading and writing.
- It consists of a command service that writes data and a query service that reads data, from 2 synchronized storages.
- This enables separation of both actions while also maintaining accuracy.

### Structure
- We can use Java SpringBoot to create microservices
- This image show the architectural structure of the project.

    ![Imgur](https://i.imgur.com/9uYZ2Eb.png)