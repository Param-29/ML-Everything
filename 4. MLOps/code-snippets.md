# Code-snippets

## Model deployment 

1. Step one is to get trained model in binary (pickle, etc) (with library versions used to build and train models)
2. Build functions & test predicit and load features
3. Create endpoints (REST APIs) and test if rest-apis work;

> Note: Flask (and maybe other servers) are not produciton servers; they are deployment servers we need to use a WSGI server instead

**Example:**:  GUNICON

```bash
pip install gunicorn 
gunicorn --bind=0.0.0.0:{port} {python_module}:{app_variable} 
# app_variable should store Flask object; python_module: name of the python file where code is present
```

**Packaging file as a docker container**


Read more about 

1. GUNICORN 
2. Docker & container
3. Package & envoriment managers
   1. Installing packages for devs vs production envoirment


## Prefect 

> Prefect is used for adding functionalities to your data-piplines and automating **work-flows**

Readme: [link](Prefect.md)