# beemademo

## Set-up Instructions

### 1. Create and activate new virtual env
### 2. Go to your projects directory and clone the repo ``` https://github.com/natashaa/beemademo.git ```
### 3. Navigate to beemademo directory and install requirements
```
cd beemademo
pip install -r requirements.txt

```
### 4. Run migrations ``` python manage.py migrate ```
### 5. Create superuser ``` python manage.py createsuperuser ```
### 6. Run dev server ``` python manage.py runserver ```
### 7. Login to dev server``` http://localhost:8000/admin/```

## API details

### Customer Creation
```
curl --header "Content-Type: application/json" --request POST --data '{
  "first_name": "Ben",
  "last_name": "Stokes",
  "dob": "25-06-1991"
}' http://127.0.0.1:8000/api/v1/create_customer/

```

### Quote Creation (By default, quote will be created in new state)
```
curl --header "Content-Type: application/json" --request POST --data '{
"name": "AV Life Insurance",
"type": "life-insurance",
"premium": 100,
"cover": 10000,
"customer_id": 1
}' http://127.0.0.1:8000/api/v1/quote/
```

### Quote conversion - ACCEPT Quote (New to Quoted state), returns quote-id and status in response.
```
curl --header "Content-Type: application/json" --request PUT http://127.0.0.1:8000/api/v1/quote/1/accept/
```

### Quote conversion - PAY Quote (Quoted to bound state), returns quote-id and status in response.
```
curl --header "Content-Type: application/json" --request PUT http://127.0.0.1:8000/api/v1/quote/1/pay/
```

### Policy API end points -list, detail, history (performs on Policy model with state bounded)
##### Policy is quote in bound state i.e customer has paid for the quote
```
curl --header "Content-Type: application/json" --request GET http://127.0.0.1:8000/api/v1/policies/
curl --header "Content-Type: application/json" --request GET http://127.0.0.1:8000/api/v1/policies/1/
curl --header "Content-Type: application/json" --request GET http://127.0.0.1:8000/api/v1/policies/1/history/
```

### Search for customer and policy
```
curl http://localhost:8000/api/v1/customer/?first_name=Ben
curl http://localhost:8000/api/v1/customer/?last_name=Stokes
curl http://localhost:8000/api/v1/customer/?full_name=ben%20s
curl http://localhost:8000/api/v1/customer/?dob=1991-06-25
curl http://localhost:8000/api/v1/policies/?customer_id=1
```

### Authentication
##### For users, there should be passwordless authentication based on contacts like email, phone
##### For customer, session authentication so they can login and check their policy documents

