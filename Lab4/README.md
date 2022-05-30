# Software architecture lab 4: Loan management
This is lab 4 of [software architecture lab](https://insatunisia.github.io/TP-ArchLog/tp4/)
- work by Melek Elloumi

## Application description
- The objective of this lab is to define the architecture and develop a demo of a loan management module for an
existing bank application that takes documents info from clients and approves them to form an agreement.
- The whole process contains 4 successive subprocesses. Each one take an input from the previous subprocess and deliver
an output to the next subprocess.
- Risk management and commercial service uses OCR (Optical Character Recognition) in order to read the text from the
scanned documents they receive.
- These subprocesses need to be automated.

## Architecture

### Microservices?

- The first architecture solution that comes to mind is using microservices for each subprocess.
- This makes each subprocess independent of the other, it increases maintainability and performances.
- It can be automated from start to finish.
- GLx team can be divided for each microservice which speeds up the development time.
- OCR is also hosted in a microservice which risk management and commercial service microservices uses.

### Problem with microservices

- This solution may eventually work but the microservices are heavily interconnected which with increasing loads of
documents and requests, it can lead to failure or long process times.
- Each subprocess isn't complex and deploying a microservice for it to execute a function or two is costly
and complicating.
- How to improve the solutions? By using serverless microservices.

### Serverless Microservices
- Serverless microservices are cloud-based services that use serverless functions to perform highly 
specific roles within an application. Serverless functions, which execute small segments of code 
in response to events, are modular and easily scalable, making them well-suited for microservice-based
architectures.
- We can consider each subprocess interaction as an event. A broker will handle these events which serverless functions 
would react to and execute their code.
- The client will interact with the service through this broker by sending the document as an event and receiving notifications.
- This enables automation even more by making the serverless functions rely on a broker.
- The process time can be improved by deploying more brokers.

### Structure
- To deploy serverless microservices, we can use AWS lambda or Azure functions.
- We can use Redis Streams as a broker for events between microservices.
- This image show the architectural structure of the project.

    ![Imgur](https://i.imgur.com/Vp8ggr2.png)