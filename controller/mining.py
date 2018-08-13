#!/usr/bin/env python

from main import block_chain
from flask import Flask
from service import mining
from controller import transaction

node = Flask(__name__)

@node.route('/mine', method='GET')
def mine():
    miners_address = mining.get_miners_address()
    last_node = block_chain[len(block_chain)-1]
    last_proof = last_node.data['proof-of-work']

    proof = mining.proof_of_work(last_proof)
    transaction.this_nodes_transactions.append({
        "from": "network",
        "to": miners_address,
        "amount": 1
    })


