import csv
from os import listdir
from os.path import isfile, join

import requests
from requests.exceptions import ConnectionError
from celery import task
from django.conf import settings

from .models import ServiceMonitorLog


def log_status(site: str, url: str, is_up: bool):
    """
    Log ststus 
  
    Save the status into a database for every url check.
  
    Parameters: 
    site (str): Site Name
    url (str): Url of the site
    is_up (bool): The status of the url check
    """
    ServiceMonitorLog.objects.create(site=site, url=url, is_up=True)

def get_url_data(csv_file_path: str):
    """
    A generator function to read CSV

    Read the CVS file and extract the url and site name.

    Parameters:
    csv_file_path (str): Path of the CSV file

    Returns:
    Generator
    """
    with open(csv_file_path, "r", encoding="latin-1") as url_records:
        for url_records in csv.reader(url_records):
            yield url_records

def check_status(site: str, url: str):
    """
    Check Url status

    Check Url status by sending a get request, and log the request result.

    Parameters:
    site (str): Site name
    url (str): Site Url
    """
    try:
        response = requests.get(url)
        if response.status_code == 200:
            log_status(site, url, True)
        else:
            log_status(site, url, False)
    except ConnectionError:
        log_status(site, url, False)

def monitor_urls():
    """
    Monitor Urls

    Read the csv file form path and process request
    """
    all_files = [f for f in listdir(settings.CSV_PATH) if isfile(join(settings.CSV_PATH, f))]
    if all_files:
        for url in get_url_data(settings.CSV_PATH+all_files[0]):
            check_status(url[0], url[1])

@task(name='monitor_urls_task')
def monitor_urls_task():
    """
    Long running process

    A long running background task runes every 10 minuts
    """
    monitor_urls()
    