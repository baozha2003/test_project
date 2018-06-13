from configparser import ConfigParser
import codecs
import os

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))) + '\config.ini'
config = ConfigParser()
config.read_file(codecs.open(path, "r", "utf-8-sig"))


def receive_email():
    receive_email = config.get("mail", "receive_email")
    return receive_email


def receive_emails():
    receive_email = config.get("mail", "receive_email")
    receive_emails = receive_email.split(',')
    return receive_emails


def chromedriver_location():
    chromedriver_location = config.get("chromedriver", "chromedriver_location")
    return chromedriver_location


if __name__ == "__main__":
    print(receive_email())
    print(receive_emails())
    print(chromedriver_location())
