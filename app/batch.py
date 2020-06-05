import datetime

import pandas
import time

from .import_tool import get_ticket
from flask import current_app


#batch to retrieve price of ticket for all departure station
#
#frequency: every night
def batch_ticket():

    get_ticket(datetime.datetime.now().replace(hour=datetime.datetime.now().hour+1),87113001)


