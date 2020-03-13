import configparser

env = configparser.RawConfigParser()
# The path where we fill information about DB
configFilePath = 'settings_confs_files/environnement.txt'
env.read(configFilePath)
