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


Prefect is made up of flows and tasks !! 

**Flow** (& subflows)
> Sequence of individual parts of data-pipeline which we need to run (and get functionality for)
> Function that does many tasks

```python3
from prefect import flow

@flow
def my_favorite_function():
    print("What is your favorite number?")
    return 42

print(my_favorite_function())

```
**Task**
> Individual (function) work executed within flows

Unit function/step in flow; adding them is helpful for 
1. Cashing outputs of tasks
2. Observability
3. easier Debugging 
4. Better Logging 
5. Option for Concuruncy (serial and parallel executions)

Converting functions inside flows to task

```python3
import requests
from prefect import flow, task

@task
def call_api(url):
    response = requests.get(url)
    print(response.status_code)
    return response.json()

@flow
def api_flow(url):
    fact_json = call_api(url)
    return fact_json

print(api_flow("https://catfact.ninja/fact"))
```


Subflows over tasks (when?)
> When you want to group tasks together

Caching of task outputs 

```python3
@task(cache_key_fn=task_input_hash, cache_expiration=timedelta(days=1))
def my_task():
   return "hello"
```

Retry tasks on failure 

```python3
@task(retries, retries_delay_seconds)
```


**Deployment**

Deploying flows on server for automated runs, continued reruns; 

Creating using CLI 

**Scheduling data work-flows**
![prefect-scheduled-deployments](images/prefect-scheduled-deployments.png)

* running scripts between time
 Using deployments 