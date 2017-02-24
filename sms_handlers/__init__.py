from sms_handlers.exception import ThereIsNoSuchHandlerException
from sms_handlers.special_handler import SmsCenterHandler, SmsTrafficHandler


def get_handler(handler_name):
    """
    This method implements abstract factory pattern.
    :param handler_name: the name of sms service
    :return: handler class
    """

    if handler_name == 'sms_center':
        handler = SmsCenterHandler()
    elif handler_name == 'sms_traffic':
        handler = SmsTrafficHandler()
    else:
        raise ThereIsNoSuchHandlerException()
    return handler
