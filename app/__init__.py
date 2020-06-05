# -*- encoding: utf-8 -*-
"""
Python Aplication Template
Licence: GPLv3
"""
import atexit
import datetime
from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler
from app import batch

app = Flask(__name__,static_folder= 'static')

app.config.update(
        DEBUG=True,
        TEMPLATES_AUTO_RELOAD=True
    )

#Configuration of application, see configuration.py, choose one and uncomment.
#app.config.from_object('configuration.ProductionConfig')
app.config.from_object('app.configuration.DevelopmentConfig')
#app.config.from_object('configuration.TestingConfig')

scheduler = BackgroundScheduler(daemon=True)
# batch to retrieve ticket price
scheduler.add_job(batch.batch_price, 'interval', minutes=30, start_date=datetime.datetime.now().replace(minute=2))
#launch sheduling thread
scheduler.start()

# Shut down the scheduler when exiting the app
atexit.register(lambda: scheduler.shutdown())

from app import views, models
