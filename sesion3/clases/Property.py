#!/usr/bin/python3

class Property:
    def __init__(self, **kwargs):
        self.properties = kwargs

    def get_properties(self):
        return self.properties

    def get_property(self, key):
        return self.properties.get(key, None)

def main():
    object = Property(name = 'python',year = 2022)
    print(object.get_property('name'))
    print(object.get_property('year'))

if __name__ == "__main__":
	main()
