import configparser

def get_password():
    data = configparser.ConfigParser()
    data.read('password.ini')
    password = data["password"]["password"]
    name_bd = data["password"]["name_bd"]
    user = data["password"]["user"]
    return [password, name_bd, user]