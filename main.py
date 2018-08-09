#!/usr/bin/env python
from Model.Block import Block
from Service.BlockFunctions import *
from datetime import datetime

def run():
    block_chain = [initialize_genesis_block()]
    max_number_of_blocks = 20
    previous_block = block_chain[0]

    for i in range(0, max_number_of_blocks):
        block_to_add = get_next_block(previous_block)
        block_chain.append(block_to_add)
        previous_block = block_to_add
        print("Block Added : " + str(block_to_add.index))
        print("Block's Hash: " + block_to_add.hash)

    print("Block Chain Transaction Successful !")

if __name__ == '__main__':
    run()