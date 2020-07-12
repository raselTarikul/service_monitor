import csv
import types
import os
from unittest import mock

from django.test import TestCase
from django.test import Client
from django.urls import reverse
from django.conf import settings

from monitor.apps.lrp.models import ServiceMonitorLog
from monitor.apps.lrp.tasks import (
    log_status, get_url_data, check_status, monitor_urls)


class MockResponse(object):
    """
    Mock response object for mocking
    """

    def __init__(self, json_data, status_code):
        self.json_data = json_data
        self.status_code = status_code

    def json(self):
        return self.json_data


class TestTasks(TestCase):

    def setUp(self):
        self.url = reverse('summary')
        self.client = Client()
        self.csv_path = settings.CSV_PATH + 'mycsv.csv'
        if os.path.exists(self.csv_path):
            os.remove(self.csv_path)

        with open(self.csv_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['test one', 'http://testone.com'])
            writer.writerow(['test two', 'http://testtow.com'])
            writer.writerow(['test three', 'http://testthree.com'])

    def test_log_status(self):
        log_status('create test', 'http://createtest.com', True)
        self.assertEqual(ServiceMonitorLog.objects.filter(
            site='create test').count(), 1)

    def test_get_url_data(self):
        data = get_url_data(self.csv_path)
        self.assertIsInstance(data, types.GeneratorType)

    @mock.patch('monitor.apps.lrp.tasks.requests.get')
    def test_check_status(self, mock_request):
        mock_request.return_value = MockResponse({}, 200)
        check_status('test unique', 'http://testone.com')
        obj = ServiceMonitorLog.objects.filter(site='test unique')
        self.assertEqual(obj.count(), 1)
        self.assertTrue(obj.first().is_up)

    @mock.patch('monitor.apps.lrp.tasks.requests.get')
    @mock.patch('monitor.apps.lrp.tasks.get_url_data')
    def test_monitor_urls(self, get_url_data, mock_request):
        ServiceMonitorLog.objects.all().delete()
        get_url_data.return_value = [('test one', 'http://testone.com'),
                                     ('test two', 'http://testtow.com'),
                                     ('test three', 'http://testthree.com')]
        mock_request.return_value = MockResponse({}, 200)
        monitor_urls()
        self.assertEqual(ServiceMonitorLog.objects.all().count(), 3)
