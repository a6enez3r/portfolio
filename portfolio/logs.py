"""
    logs.py: contains function to configure & create loggers
"""
import json
import logging

import requests


class SlackerLogHandler(logging.Handler):
    """
    Slack log handler that emits error + messages
    to a slack channel using incoming webhook URL.

    Args
    ----
        - webhook_url (str): The URL of the incoming webhook for the Slack channel.

    Attributes
    ----------
        - webhook_url (str): The URL of the incoming webhook for the Slack channel.
    """

    def __init__(self, webhook_url: str):
        """
        Initializes a new instance of the SlackerLogHandler.

        Args
        -----
            - webhook_url (str): The URL of the incoming webhook for the Slack channel.

        """
        super().__init__()
        self.webhook_url = webhook_url

    def slack_message(self, title, value) -> None:
        """
        Send a message to a Slack channel using incoming webhooks

        Args
        -----
            - title (str): title of message
            - value (str): body of the message

        Returns
        -------
            - None
        """
        hook = self.webhook_url
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

        resp = requests.post(
            hook, data=json.dumps(payload), headers=headers, timeout=30
        )
        print("Response: " + str(resp.status_code) + "," + str(resp.reason))

    def emit(self, record: str):
        """
        Emit logs and send message to a Slack channel

        Args
        -----
            - record (str): log record

        Returns
        -------
            - None
        """
        message = self.format(record)
        self.slack_message(
            "Tunez - Logs", message
        )  # pylint: disable=too-many-function-args
