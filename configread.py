from configparser import ConfigParser

#create object of configparser
config=ConfigParser()

# Reading data from config file
config.read("C:/projects/practice/python/pytest/utils/config.cfg")


print(config.get("data","name"))