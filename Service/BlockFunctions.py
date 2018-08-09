#!/usr/bin/env python
from Model.Block import Block
from datetime import datetime

def initialize_genesis_block():
    return Block(0, datetime.now(), "Genesis Bloc","0")


def get_next_block(previous_block):
    next_block = Block()
    next_block.index = previous_block.index + 1
    next_block.timestamp = datetime.now()
    next_block.data = "Block Number: " + str(next_block.index)
    next_block.hash = previous_block.generate_hash()
    next_block.previous_hash = previous_block.hash
    return  next_block

