import logging
import datetime
import os


def logger_config(name):
    now = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    path = os.path.join(os.getcwd(), 'log/{}-{}.log'.format(name.lower(), now))
    fh = logging.FileHandler(path)
    fh.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s >>> %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    return fh, ch


def logger(name):
    log = logging.getLogger(__name__)
    log.setLevel(logging.DEBUG)
    fh, ch = logger_config(name)
    log.addHandler(fh)
    # log.addHandler(ch)
    return log