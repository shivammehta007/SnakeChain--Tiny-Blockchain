#!/usr/bin/env python
import configparser
from configurations import ApplicationConfiguration
import os

def proof_of_work(last_proof):
    '''
    This method return a proof when the new proof will be divisble by 9 and the last proof of the transaction
    :param last_proof: Last proof of transaction
    :return: Next proof of the transaction
    '''
    incrementor = last_proof + 1
    while not (incrementor % 9 == 0 and incrementor % last_proof == 0):
        incrementor += 1
    return incrementor


def get_miners_address():
    mining_configuration_file = os.path.join(os.getcwd() , ApplicationConfiguration.resources_folder, ApplicationConfiguration.mining_configuration)
    mining_config = configparser.ConfigParser()
    mining_config.read(mining_configuration_file)
    return mining_config.get('Mining' , 'miners-address')


