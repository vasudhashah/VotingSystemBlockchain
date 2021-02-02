from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
# Create your views here.
import json
from BlockchainApp.blockchain.blockchain import Blockchain
from BlockchainApp.wallet.wallet import Wallet
from BlockchainApp.wallet.transaction import Transaction
from BlockchainApp.wallet.transaction_pool import TransactionPool
from BlockchainApp.config import BID_AMOUNT
from BlockchainApp.pubsub import PubSub


blockchain=Blockchain()
wallet=Wallet(blockchain)
transaction_pool=TransactionPool()
pubsub=PubSub(blockchain, transaction_pool)
draws = []
def route_blockchain(request):
    return HttpResponse(blockchain)

def route_blockchain_range(request):
    start = 0
    end = 10

    return HttpResponse(blockchain[::-1][start:end])

def route_blockchain_length(request):
    return HttpResponse(len(blockchain.chain))


def route_blockchain_mine(request):
    transaction_data = transaction_pool.transaction_data()
    transaction_data.append(Transaction.reward_transaction(wallet).to_json())
    blockchain.add_block(transaction_data)
    block = blockchain.chain[-1]
    pubsub.broadcast_block(block)
    transaction_pool.clear_blockchain_transactions(blockchain)

    return HttpResponse(block)

#problem aari
def route_wallet_transact(request):
    if request.method=='POST':
        aadhar_no = request.POST['selected_candidate']
        print(aadhar_no)
        transaction = transaction_pool.existing_transaction(aadhar_no)

        if transaction:
            transaction.update(wallet,
            aadhar_no,
            1
            )
        else:
            transaction = Transaction(
                wallet,
                aadhar_no,
                1
                )

        print(f'transaction.to_json(): {transaction.to_json()}')
        pubsub.broadcast_transaction(transaction)

        return HttpResponse(f'wallet balance: {wallet.to_json()}')

def route_transactions(request):
    return HttpResponse(transaction_pool.transaction_data())
