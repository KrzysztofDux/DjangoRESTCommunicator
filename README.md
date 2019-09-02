# DjangoRESTCommunicator
A learning project, simple communicator based on REST.

How to start:
You have to have docker compose installed on your machine.
Open terminal in the main catalog and run
```sh
docker-compose up
```
It will start the application.
(if it fails you probably need to free up port 8000 or change the port settings in docker-compose.yaml file)

How to use it:
To acquire credentials send empty GET request to the endpoint
```
/dispatch/login
```
(this element is just a scaffolding for now, to be replaced with safe approach in the future)
JSON with two fields will be returned:
```
{"identity": "[8 characters long number]", "password": "[8 characters alphanumeric]"}
```
To send a message send POST request to the endpoint
```
/dispatch/send_message
```
with four body parameters:
  - ```author``` which is your identity number
  - ```password``` which is your password
  - ```addressee``` which is your addresse identity number
  - ```content``` which is the content of message to be sent

to aqcuire messages that has been sent to you send POST request to the endpoint
```
/dispatch/get_messages
```
with two body parameters:
  - ```addressee``` which is your identity number
  - ```password``` which is your password
  
Notice that after the message is downloaded it's removed from the app's database, so each message will be downloaded only once.

Currently there's also a
```dispatch/get_users```
endpoint, that returns all the users with their passwords.
It's convenient for testing, but of course will no longer be available after passwords are properly handled.

For testing purposes you can run [test client](https://github.com/KrzysztofDux/DjangoRESTCommunicatorTestClient) in parallel windows and send messages between them.
