import time

import geocoder
import folium
import pandas
import requests
from shapely import geometry
from ..models import Station
from .train_query import find_ticket

import datetime

data_to_store_df = pandas.DataFrame(
        columns=["destination", "departure_date", "arrival_date", "duration", "number_of_segments", "price", "currency",
                 "transportation_mean"])


def _string_from_datetime(date_datetime):
    date = date_datetime
    string = str(date.day)+"/"+str(date.month)+"/"+str(date.year)+" "+str(date.hour)+":"+str(date.minute)
    # DD/MM/YYYY HH:mm
    return string

def get_ticket(*args):
    print('Start batch to import trip prices...')
    start = time.time()
    if len(args) == 0:
        print('No args found. Exit')
        raise ValueError
    #get date from arguments
    if isinstance(args[0], datetime.datetime):
        date = args[0]
    else:
        raise ValueError

    if len(args) > 1:
        #case 1: treat one uic
        if isinstance(args[1], int):
            departure_id = args[1]
            print('Import price for station n°',args[1],'...')
            connections = Station.from_uic(departure_id)._get_connections()
            find_ticket(date,departure_id,connections)
            print(time.time() - start)
        #case 2: treat a list of uic
        elif isinstance(args[1], list):
            departure_id = args[1]
            print('Import price for stations', args[1], '...')
            for station in args[1]:
                connections = Station.from_uic(departure_id)._get_connections()
                find_ticket(date,station,connections)
                print(time.time() - start)
    print(time.time() - start)


