# Forecast-Microservices
By Melek Elloumi, Mohamed Ben Salah and Mohamed Karim Mellouli, GL4

## Demo:
- This is a demo of a forecast-planning application to study a microservice-based architecture.
- The demo is composed of 3 microservices made with Flask in python.
    - Forecast UI for web interface
    - Forecast Backend for fetching data from mongodb database
    - Security for authentification
- We chose flask because it's a microframework, it's lightweight and quick to setup api routes,
and it's based on python which opens up a lot of libraries for forecasting.

    ### Execution

    ![2014-10-22 11_35_09](https://j.gifs.com/OgoGgG.gif)

## Architecture:
- This is part of a [software architecture lab](https://insatunisia.github.io/TP-ArchLog/tp3/)
- The application is devided into 3 main applications, forecast and planning applications are hosted and provide
2 different services and a headless application that runs every week to generate forecasts and plans in the databases.
- This solution have non-functional requirements: security, maintability, flexibility and performance.
- The microservice architecture is best suited for this type of solution:
  - We can reuse planning and forecast applications for other solutions that require these modules.
  - It makes increasing the scalabilty easy to manage which improve performances
  - We can apply non-functional implementations like security for any microservice.
- This image show the architectural structure of the project. The demo contains only 1 use case of the forecast application
alongside security.

    ![Imgur](https://i.imgur.com/RyuMvX2.png)