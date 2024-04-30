class BiDict:

    def __init__(self):
        self._map01: dict = {}
        self._map02: dict = {}

    def add(self, elem01, elem02):
        self._map01[elem01] = elem02
        self._map02[elem02] = elem01

    def get(self, elem):
        vals = []
        try:
            vals.append(self._map01[elem])
        except:
            pass

        try:
            vals.append(self._map02[elem])
        except:
            pass

        return vals
