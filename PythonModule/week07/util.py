import time
import datetime
from inspect import getcallargs

logger = []

def time_decorator(func):

    def wrapper(*args, **kwargs):
        before = time.time()
        value = func(*args, **kwargs)
        print(round(time.time() - before))
        return value

    return wrapper

def logging_decorator(__list):

    def decorator(func):

        def wrapper(*args, **kwargs):
            time = datetime.datetime.now()
            res = func(*args, **kwargs)
            __list.append({"name": func.__name__,
                           "arguments": getcallargs(func, *args, **kwargs),
                           "call_time": time,
                           "result": res})
            return res

        return wrapper

    return decorator

def request_handler():
    import requests
    import json
    import pickle

    URL = "https://webhook.site/2bf6920d-8bc3-4424-a1e9-f14c6c54477d"

    users = requests.get("https://jsonplaceholder.typicode.com/users")
    comments = requests.get("https://jsonplaceholder.typicode.com/comments")
    posts = requests.get("https://jsonplaceholder.typicode.com/posts")

    statistics = [{"id": user["id"],
                   "username": user["username"],
                   "email": user["email"],
                   "posts": sum([1 for post in posts.json() if post["userId"] == user["id"]]),
                   "comments": sum([1 for comment in comments.json() if comment["email"] == user["email"]])}
                   for user in users.json()]

    response = requests.post(URL, data = json.dumps({"statistics": statistics}))

    with open("result.pickle", mode="wb") as f:
        pickle.dump(response, f)
