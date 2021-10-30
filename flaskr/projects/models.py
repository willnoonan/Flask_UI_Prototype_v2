from flaskr.util import GenPage


class Proj(GenPage):
    global_id = 0
    def __init__(self, name):
        super().__init__(name)
        Proj.global_id += 1
        self.id = Proj.global_id