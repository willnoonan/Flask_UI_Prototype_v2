from flaskr.util import GenPage


class Config(GenPage):
    global_id = 0
    def __init__(self, name):
        super().__init__(name)
        Config.global_id += 1
        self.id = Config.global_id