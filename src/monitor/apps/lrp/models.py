from django.db import models


class ServiceMonitorLog(models.Model):
    """
    Service motior Log

    A Service monitor log thats repregents the Logging the site status with
    auto added date and time
    """
    site = models.CharField(max_length=255)
    url = models.URLField(max_length=255)
    is_up = models.BooleanField()
    log_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.site
