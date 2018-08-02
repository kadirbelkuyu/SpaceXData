import requests
import json


class SpaceX():
    rocket_name = None
    launch_year = None
    launch_success = None

    def __init__(self):
        self.rocket_name = None
        self.launch_year = None
        self.launch_success = None
        print("Welcome")
        menu= input("""Please select your operation.
              1-Search by the rocket name
              2- Search by the launch year
              3-Search by the launch success              
              """)
        if menu=="1":
            search(rocket_name)
        if menu=="2":
            search(launch_year)
        if menu=="3":
            search(launch_success)

SpaceX()