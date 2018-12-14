class Person:
    def __init__(self, id):
        self.id = id


sam = Person(100)
sam.__dict__['age'] = 49

result = sam.age + len(sam.__dict__)

print(result, sam.__dict__)
