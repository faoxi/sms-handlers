import json

import logging
import requests
from abc import ABCMeta, abstractmethod, abstractproperty


class AbstractHandler(object):
    """
    This is basic sms handler
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def send(self, phone, message):
        """
        :param phone: phone of subscriber.
        :param message: message to sent.
        """

    @abstractproperty
    def url(self):
        """
        url for sending
        This method has to send message and parse the response.
        """

    @abstractmethod
    def _collect_message_to_send(self, phone, message):
        """
        :param phone: phone to send message.
        :param message: a text of the message.
        :return: complete message.
        """

    @abstractmethod
    def _handle_response(self, response):
        """
        logging dict to response
        This method doesn't know the implementation of response. It is just a dict.
        """


class JsonHandler(AbstractHandler):
    __metaclass__ = ABCMeta

    def send(self, phone, message):
        ready_to_send_message = self._collect_message_to_send(phone, message)
        response = requests.post(self.url, json=ready_to_send_message)

        if response.status_code == 200:
            self._handle_response(json.loads(response.content))
        else:
            logging.error('Status code of service {url} is {status_code}'
                          .format(url=self.url,
                                  status_code=response.status_code))

