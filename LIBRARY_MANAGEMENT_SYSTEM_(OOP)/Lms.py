import json

class Books:
    def __init__(self):
        self._books = self.__read_json('books.json')
    def __read_json(self, path):
        with open(path, 'r') as f:
            return json.load(f)
    def __write_json(self, path, data):
        with open(path, 'w') as f:
            json.dump(data, f, indent=4)
    def display_books(self):
        pass
    



book = Books()
print()










