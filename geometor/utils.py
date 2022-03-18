'''utils'''
import logging

def log_init(name):
    filename = f'logs/{name}.log'
    with open(filename, 'w'):
        pass

    logging.basicConfig(
            filename=f'logs/{name}.log', 
            filemode='w', 
            encoding='utf-8', 
            level=logging.INFO
            )
    logging.info(f'Init {name}')

def print_log(txt=''):
    print(txt)
    logging.info(txt)

# time *********************
import datetime
from timeit import default_timer as timer

def elapsed(start_time):
    secs = timer() - start_time
    return str(datetime.timedelta(seconds=secs))


# files and folders **********************
import os as os
