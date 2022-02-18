- Update `config_master.yml`. Change its hostname as per the instance you want to test.
- command to run master: (you will see all req statistics here)
```
locust --config=config_master.yml
```
- command to start workers: (open multiple tabs for multiple workers)
```
locust --config=config_worker.yml 
```
