"""
    logs.py: contains function to configure & create loggers
"""
import logging
import json
import requests


class SlackerLogHandler(logging.Handler):
    def __init__(self, webhook_url):
        super().__init__()
        self.webhook_url = webhook_url

    def slack_message(self, webhook_url, title, value):
        """
        send message to slack channel (using incoming webhooks)

        params:
            - webhook_url
            - title
            - value
        returns
            - none
        """
        hook = webhook_url
        headers = {"content-type": "application/json"}
        payload = {
            "attachments": [
                {
                    "fallback": "",
                    "pretext": "",
                    "color": "#f4f4f4",
                    "fields": [{"title": title, "value": value, "short": False}],
                }
            ]
        }

        r = requests.post(hook, data=json.dumps(payload), headers=headers)
        print("Response: " + str(r.status_code) + "," + str(r.reason))

    def emit(self, record):
        message = self.format(record)
        self.slack_message(self.webhook_url, "Portfolio - Logs", message)
