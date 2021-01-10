from locust import HttpUser, TaskSet, task

class UserBehavior(TaskSet):
    @task
    def get_favicon(self):
        self.client.get("/favicon.ico")
    
    @task
    def get_work(self):
        self.client.get("/")
    
    @task
    def get_about(self):
        self.client.get("/about")
    
    @task
    def get_resume(self):
        self.client.get("/resume")

class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    