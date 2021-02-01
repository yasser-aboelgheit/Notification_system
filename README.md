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
* create two queues in celery "tasks" and "tasks2" where "tasks" has higher priority, this queue is for tasks that may go ```diff @@ obsolete @@ ``` such as dropoff location notification 
- rate limit for celery tasks 10/m and max_retries=3
