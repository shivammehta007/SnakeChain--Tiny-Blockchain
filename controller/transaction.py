#!/usr/bin/env python
from flask import Flask
from flask import request

node = Flask(__name__)

this_nodes_transactions = []


@node.route('/transaction', methods=['POST'])
def transaction():
    if request.method == 'POST':
        new_transaction = request.get_json()
        this_nodes_transactions.append(new_transaction)
        print("New Transaction : ")
        print("Transaction From : {}".format(new_transaction['from']))
        print("Transaction To : {}".format(new_transaction['to']))
        print("Amount : {}".format(new_transaction['amount']))

        return "Transaction Completed Successfully!"
