import random
import string
from locust import HttpUser, task, between

class MyReqRes(HttpUser):
    """
    Custom Locust user class for simulating login, sign-up, and homepage browsing actions.
    
    Attributes:
        host (str): Base URL of the target application.
        wait_time (function): Function that returns a random wait time between requests.
    """

    host = "http://www.sarakel.me"
    wait_time = between(1, 6)

    @task
    def login_signUp_homepage(self):
        """
        Task to simulate user login, sign-up, and browsing the homepage.
        """
        # Simulate user login
        self.login()

        # Simulate user browsing behavior
        self.index_page()

        # Simulate user sign-up
        self.signup()

    def index_page(self):
        """
        Simulate user browsing the homepage of the website.
        """
        self.client.get("/")

    def login(self):
        """
        Simulate user login.
        
        This method sends a POST request to the login endpoint with predefined credentials.
        """
        payload = {
            "emailOrUsername": "TestingTeam2025",
            "password": "Testing@2025"
        }
        headers = {
            "Content-Type": "application/json"
        }
        response = self.client.post("/api/login", json=payload, headers=headers)
        if response.status_code == 200:
            print("Login successful")
        else:
            print(f"Login failed with status code: {response.status_code}")

    def createEmail(self):
        """
        Generate a random email address.
        
        Returns:
            tuple: Randomly generated username and email address.
        """
        # Generate a random string of letters and digits for the username
        username = ''.join(random.choices(string.ascii_letters + string.digits, k=10))

        # Add a domain name
        email = username + '@yopmail.com'
        return username, email

    def createPasword(self):
        """
        Generate a random strong password.
        
        Returns:
            str: Randomly generated strong password.
        """
        char_set = string.ascii_letters + string.digits + string.punctuation
        # Generate a random password of the specified length
        password = ''.join(random.choice(char_set) for i in range(12))
        return password

    def signup(self):
        """
        Simulate user sign-up.
        
        This method generates random email, password, and username for a new user,
        constructs the payload for the sign-up request, and sends the request to the sign-up endpoint.
        """
        # Generate random email, password, and username for the new user
        username, email = self.createEmail()
        password = self.createPasword()

        # Construct payload for sign-up request
        payload = {
            "email": email,
            "password": password,
            "username": username
        }

        # Send sign-up request
        headers = {
            "Content-Type": "application/json"
        }
        response = self.client.post("/api/signup", json=payload, headers=headers)

        # Check if sign-up was successful
        if response.status_code == 200:
            print(f"Sign-up successful for user: {email}")
        else:
            print(f"Sign-up failed with status code: {response.status_code}")
