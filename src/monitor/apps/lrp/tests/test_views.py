from unittest import mock

from django.test import TestCase
from django.test import Client
from django.urls import reverse

from monitor.apps.lrp.models import ServiceMonitorLog

class TestView(TestCase):
    def setUp(self):
        self.url = reverse('summary')
        self.client = Client()

        ServiceMonitorLog.objects.create(site='test one', url='http://testone.com', is_up=True)
        ServiceMonitorLog.objects.create(site='test two', url='http://testwo.com', is_up=False)
        ServiceMonitorLog.objects.create(site='test three', url='http://testhree.com', is_up=True)
        ServiceMonitorLog.objects.create(site='test one', url='http://testone.com', is_up=True)
        ServiceMonitorLog.objects.create(site='test two', url='http://testwo.com', is_up=False)
        ServiceMonitorLog.objects.create(site='test three', url='http://testhree.com', is_up=True)
        ServiceMonitorLog.objects.create(site='test one', url='http://testone.com', is_up=True)
        ServiceMonitorLog.objects.create(site='test two', url='http://testwo.com', is_up=False)
        ServiceMonitorLog.objects.create(site='test three', url='http://testhree.com', is_up=True)
    
    def test_summary(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['total_verified'], 9)
        self.assertEqual(response.json()['total_up'], 6)
        self.assertEqual(response.json()['total_down'], 3)
        self.assertEqual(response.json()['unique_sites'], 3)
        self.assertEqual(response.json()['unique_up_sites'], 2)
        self.assertEqual(response.json()['unique_down_sites'], 1)
