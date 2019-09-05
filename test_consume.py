from consumer import Consumer
from functools import partial
import traceback
import json

# If you do not use partial when passing the callback function
# the _consume_message private method in the Consumer class will see a NoneType
# https://docs.python.org/3/library/functools.html#functools.partial

exchange_options = {'passive': False,  # Perform a declare or just check to see if it exists
                    'durable': True,  # Survive a reboot of RabbitMQ
                    'autoDelete': False,  # Remove when no more queues are bound to it
                    'internal': False  # True allows only other exchanges to publish to this exchange
                    }

queue_options = {'passive': False,  # Perform a declare or just check to see if it exists
                 'durable': True,  # Survive a reboot of RabbitMQ
                 'autoDelete': False,  # Remove when no more queues are bound to it
                 'exclusive': False,  # Queue can be shared across connections
                 }

amqp_config = {'exchangeName': 'e.message.created',
               'exchangeType': 'topic',
               'exchangeOptions': exchange_options,
               'routingKey': 'message.created',
               'userName': 'guest',
               'password': 'guest',
               'host': 'localhost',
               'port': '5672',
               'virtualHost': '/',
               'queueName': 'q.message.created',
               'queueOptions': queue_options
               }


def callback(body):
    if 'bytes' in str(type(body)):
        new_body = body.decode('utf-8')
        try:
            parsed_json = json.loads(new_body)
            for item in parsed_json:
                print(parsed_json[item])
        except Exception as e:
            print(repr(e))
            traceback.print_exc() # WHAT DOES THIS DO ?
            raise e


reader = Consumer(amqp_config)
reader.enter()
reader.consume(partial(callback, ))
