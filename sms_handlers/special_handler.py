import json
import logging
from abc import ABCMeta
from sms_handlers.handler import JsonHandler

logging.basicConfig(format=u'%(levelname)-8s [%(asctime)s] %(message)s', level=logging.DEBUG)


class SpecialHandler(JsonHandler):
    """
    The interface both of the services are the same. Only urls is different.
    """

    __metaclass__ = ABCMeta

    def _collect_message_to_send(self, phone, message):
        return json.dumps({
            "phone": phone,
            "message": message
        })

    def _handle_response(self, response):
        if response.get('status') == 'ok':
            logging.info('The message has been sent to {phone}'.format(phone=response.get('phone')))
        else:
            logging.error('{error_msg} {error_code} {phone}'
                         .format(error_msg=response.get('error_msg'),
                                 error_code=response.get('error_code'),
                                 phone=response.get('phone')))


class SmsCenterHandler(SpecialHandler):
    """
    Sms center
    """
    url = 'http://smsc.ru/some­api/message/'


class SmsTrafficHandler(SpecialHandler):
    """
    Sms traffic
    """
    url = 'http://smstraffic.ru/super­api/message/'