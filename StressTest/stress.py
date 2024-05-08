from locust import User, task, constant

class Myscript(User):
    wait_time = constant(1)

    @task
    def launch(self):
        print("Launching URL")

    @task
    def search(self):
        print("Searching")    