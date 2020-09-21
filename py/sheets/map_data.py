class MapData:
    def __init__(self, list_keys, row_data, cell, column):
        self.list_keys = list_keys
        self.data = row_data
        self.cell = cell
        self.col = column
        self.keys = []
        self.value = True if cell.value else False

    def find_key(self):
        key_to_find = self.list_keys[self.col]
        if self.col == 0: 
            self.keys = ["loginCredentials", "username"]
        elif self.col == 1:
            self.keys = ["loginCredentials", "password"]
        else: 
            feature_sets = self.data["featureSets"]
            self.keys.append("featureSets")
            
    def _find(self, data, key):
        for obj in data:
            for k, v in (dic.items() if isinstance(value, dict) else 
                enumerate(value) if isinstance(value, list) else []):
                if k == key:
                    self.keys.append(k)
                elif isinstance(v, (dict, list)):
                    for result in find(key, v):
                        yield result

    def change_key_value(self):
        self.find_key()
        if self.get_nested(self.data, self.keys):
            for k, v in 
        else:
            return 'Not working'

    def get_nested(self, data, keys):
        value = ""
        if data and keys:
            element  = keys[0]
            if element:
                value = data.get(element)
                if len(keys) == 1:
                    return value
                else:
                    if isinstance(value, dict):
                        self.get_nested(value, keys[1:])
                    elif isinstance(value, list):
                        value = value[0]
                        self.get_nested(value, keys[1:])
        return value

#backtracking