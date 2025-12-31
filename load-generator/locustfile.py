from locust import HttpUser, task, between

class User(HttpUser):
    wait_time = between(1, 3)

    @task
    def register(self):
        self.client.get("/register")
