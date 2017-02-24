import sms_handlers

sms_center_handler = sms_handlers.get_handler('sms_center')
sms_center_handler.send(phone='12345', message='adasd')

sms_traffic_handler = sms_handlers.get_handler('sms_traffic')
sms_traffic_handler.send(phone='1235', message='adasd')

sms_traffic_handler = sms_handlers.get_handler('sms_trafficd')