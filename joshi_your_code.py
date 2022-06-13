from requests import request
from time import time, sleep
from multiprocessing import Process


def hit_the_link():
    response = request(method='GET', url='https://www.google.com/')
    print(response)


while True:
    sleep(60 - time() % 60)  # This will make your program sleep for 60 seconds
    Process(target=hit_the_link).start()
