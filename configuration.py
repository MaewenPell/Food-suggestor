import configparser


def main():
    configFilePath = './environnement.txt'
    env.read(configFilePath)


env = configparser.RawConfigParser()
main()
