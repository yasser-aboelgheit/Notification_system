# Notification_system
Notification service based on Django Rest framework

## Technologies

* Django Rest Framework: Framework based on python used to create APIs 
* Reddis: message broker
* Celery: task queue software
* Docker: containerization
* Swagger: API documentation
* SQLite3: Database

## APIs Documentation
* Navigate to http://localhost:8000/doc, the url for swagger which is a service for automatic documentation of APIs.
* Note the file swvl.postman_collection.json which is a postman collection I created for this task, you can easily import it and find a saved response for each API

## Architecture

* Table in the database for notifications which notifications' templates are saved
* create two queues in celery "tasks" and "tasks2" where "tasks" has higher priority, this queue is for tasks that may go **obsolete** such as dropoff location notification 
- rate limit for celery tasks 10/m and max retries is 3 for each task
- To make things easier on running the project it loads a record for notifications table from fixture created already to save you the trouble of populating the database

## Installation

after cloning the project and making sure that docker-compose is up and running
use `docker-compose build`
then `docker-compose up`

## Project UML
![my_project_visualized](https://user-images.githubusercontent.com/21153250/106403454-7db62500-6437-11eb-9031-5cc3af281ba4.png)

## Test
 Use `docker-compose run test` to run tests
