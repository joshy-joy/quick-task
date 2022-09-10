# quick-task
Quick Task

### Create User API

```
curl --location --request POST 'http://127.0.0.1:5000/createUser' \
--header 'Authorization: Bearer B1n0FlddHVnfBLeAkC' \
--header 'Content-Type: application/json' \
--data-raw ' {
     "username": "Test",
     "password": "Test@123",
     "age": 26
     }'
     
 ```
