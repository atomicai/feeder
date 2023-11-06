from celery import Celery
from prime import login

import dotenv


dotenv.load_dotenv()

#app = Celery('tasks', backend='redis://localhost:6379/0', broker='amqp://guest:guest@localhost//')

#@app.task
#def add_payment():
#    return prime.payment()

#__all__ = ["add_payment"]


