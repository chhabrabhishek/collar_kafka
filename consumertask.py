from confluent_kafka import Consumer
import json
import os

class ConsumerTask(object):

    def __init__(self, conf, topic_name):
        self.consumer = Consumer(conf)
        self.topic_name = topic_name
        self.running = True

    def stop(self):
        self.running = False

    async def run(self):
        print('The consumer has started')
        self.consumer.subscribe([self.topic_name])
        while self.running:
            msg = self.consumer.poll(1)
            if msg is not None and msg.error() is None:
                print("Message consumed: " + str(msg.value()))
                data = json.loads(msg.value())
                data_json = json.dumps(data)
                with open('coordinates.json', 'w') as outfile:
                    outfile.write(data_json)
                
        self.consumer.unsubscribe()
        self.consumer.close()
