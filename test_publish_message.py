from publisher import Publisher
import json

amqp_config = {'exchangeName': 'e.message.created',
               'routingKey': 'message.created',
               'userName': 'guest',
               'password': 'guest',
               'host': 'localhost',
               'port': '5672',
               'virtualHost': '/',
               }

writer = Publisher(amqp_config)
for x in range(0,1000):
    some_dict = {'message': 'Test Message',
                 'value': x,
                 }
    some_json = json.dumps(some_dict)
    writer.publish(some_json)