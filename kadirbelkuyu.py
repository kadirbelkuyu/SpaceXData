import requests
import json
import logging
from urllib.request import urlopen

class SpaceX():
    rocket_name = None
    launch_year = None
    launch_success = None

    def __init__(self,menu):
        self.rocket_name = None
        self.launch_year = None
        self.launch_success = None
        print("Welcome")
        menu = input("""Please select your operation.
                  1-Search by the rocket name
                  2- Search by the launch year
                  3-Search by the launch success              
                  """)
        if menu == "1":
            search(rocket_name)
        if menu == "2":
            search(launch_year)
        if menu == "3":search
            search(launch_success)



    def search(self,keyword):
        pass

        # data = self.session.get('https://api.spacexdata.com/v2/launches/'.format())








