import json

from locust import HttpUser, TaskSet, task, constant

FILE_PATH = '../test_request.json'

class UserBehaviour(TaskSet):
    @task
    def start_load(self):
        req_data = self._prepare_data()
        for req in req_data:
            data = {}
            if 'body' in req.keys():
                data = req['body']
            self.client.post(req['path'], data=data, name="load_test")

    def _prepare_data(self):
        with open(FILE_PATH) as f:
            data = json.load(f)
            return data


class MyUser(HttpUser):
    wait_time = constant(0.1)
    tasks = [UserBehaviour]
