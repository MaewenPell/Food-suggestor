import configparser
import os

def main():
    print(os.getcwd())
    configFilePath = 'settings_confs_files/environnement.txt'
    env.read(configFilePath)


env = configparser.RawConfigParser()
main()
