from configparser import ConfigParser


class Config:
    def __init__(self):
        self._config = ConfigParser()
        self._config.read('config.ini')

    def __getitem__(self, item):
        return self._config[item]