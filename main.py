#!/usr/bin/env python
from service.blockfunctions import *

block_chain = [initialize_genesis_block()]

def run():
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