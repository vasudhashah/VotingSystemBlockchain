import time
from pubnub.pubnub import PubNub
from pubnub.pnconfiguration import PNConfiguration
from pubnub.callbacks import SubscribeCallback

from BlockchainApp.blockchain.block import Block
from BlockchainApp.wallet.transaction import Transaction

publish_key = 'pub-c-0c995c89-a5be-4c09-aa20-b79308b0093b'

pnconfig = PNConfiguration()
pnconfig.subscribe_key = 'sub-c-44670d6a-8e49-11ea-8dc6-429c98eb9bb1'
pnconfig.publish_key = 'pub-c-0c995c89-a5be-4c09-aa20-b79308b0093b'

'''
TEST_CHANNEL = 'TEST_CHANNEL'
BLOCK_CHANNEL = 'BLOCK_CHANNEL'
'''
CHANNELS={
    'TEST':'TEST',
    'BLOCK':'Block',
    'TRANSACTION':'TRANSACTION'
    }

class Listener(SubscribeCallback):
    def __init__(self, blockchain, transaction_pool):
        self.blockchain = blockchain
        self.transaction_pool=transaction_pool

    def message(self, pubnub, message_object):
        print(f'\n-- Channel: {message_object.channel} | Message: {message_object.message}')

        if message_object.channel == CHANNELS['BLOCK']:
            block = Block.from_json(message_object.message)
            potential_chain = self.blockchain.chain[:]
            #[0:len(self.blockchain.chain)]
            potential_chain.append(block)

            try:
                self.blockchain.replace_chain(potential_chain)
                self.transaction_pool.clear_blockchain_transactions(
                        self.blockchain
                    )
                print(f'\n -- Successfully replaced the local chain')
            except Exception as e:
                print(f'\n -- Didnot replace the chain: {e}')
        elif message_object.channel == CHANNELS['TRANSACTION']:
            transaction = Transaction.from_json(message_object.message)
            self.transaction_pool.set_transaction(transaction)
            print(f'\n -- Set the new transaction in the transaction pool')



class PubSub():
    '''
    Handles the publish/subscriber layer of the application.
    Provides communication between the nodes of the blockchain network.
    '''
    def __init__(self, blockchain, transaction_pool):
        self.pubnub = PubNub(pnconfig)
        self.pubnub.subscribe().channels(CHANNELS.values()).execute()
        self.pubnub.add_listener(Listener(blockchain, transaction_pool))

    def publish(self, channel, message):
        '''
        Publish the message object to the channel.
        '''
        self.pubnub.publish().channel(channel).message(message).sync()

    def broadcast_block(self, block):
        '''
        Broadcast a block object to all nodes.
        '''
        self.publish(CHANNELS['BLOCK'], block.to_json())

    def broadcast_transaction(self, transaction):
        '''
        Broadcast the transaction to all nodes.
        '''
        self.publish(CHANNELS['TRANSACTION'], transaction.to_json())

def main():
    pubsub = PubSub()
    time.sleep(1)

    pubsub.publish(CHANNELS['TEST'],{'foo':'bar'})

if __name__=='__main__':
    main()
