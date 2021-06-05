"""
    test_load.py: contains load tests for pages
"""
from locust import HttpUser, TaskSet, task


class UserBehavior(TaskSet):
    """
    user behavior mocking class
    """

    @task
    def get_favicon(self):
        """
        mock getting favicon
        """
        self.client.get("/favicon.ico")

    @task
    def get_work(self):
        """
        mock getting work page
        """
        self.client.get("/")

    @task
    def get_about(self):
        """
        mock getting about page
        """
        self.client.get("/about")

    @task
    def get_resume(self):
        """
        mock getting resume page
        """
        self.client.get("/resume")


class WebsiteUser(HttpUser):
    """
    register website user with mock methods
    """

    tasks = [UserBehavior]
