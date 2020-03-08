import configparser

env = configparser.RawConfigParser()
configFilePath = 'settings_confs_files/environnement.txt'
env.read(configFilePath)
