class Outer:
    class builder:
        def __init__(self):
            self.name = None
            self.age = None

        def with_name(self, name):
            self.name = name
            return self

        def with_age(self, age):
            self.age = age
            return self

        def build(self):
            return Outer(self)

    def __init__(self, inner):
        self.name = inner.name
        self.age = inner.age

    def to_dict(self):
        return {
            'name': self.name,
            'age': self.age,
        }


vimi = Outer.builder().with_age(18).with_name('vimi').build()
print(vimi.to_dict())
