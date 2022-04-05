class BuilderBase:
    def __init__(self, subclass_type):
        self.subclass_type = subclass_type

    def __getattr__(self, name):
        # if name in {'__getstate__', '__setstate__'}:
        #     return super().__getattr__(self, name)
        builder_keyword = 'with_'
        if name.startswith(builder_keyword):
            args_name = name.split(builder_keyword)[1]
            def _wrapper(builder_value):
               setattr(self, args_name, builder_value)
               return self
            return _wrapper
        raise AttributeError("'{}' object has no attribute '{}'".format(self.__class__.__name__, name))

    @classmethod
    def builder(cls):
        return BuilderBase(subclass_type=cls)

    def build(self):
        return self.subclass_type(self)


class Outer(BuilderBase):
    def __init__(self, inner):
        self.name = inner.name
        self.age = inner.age
        self.money = inner.money
        self.city = inner.city

    def to_dict(self):
        return {
            'name': self.name,
            'age': self.age,
            'money': self.money,
            'city': self.city,
        }


x = Outer.builder().with_age(18).with_name('vimi').with_money(100).with_city('guangzhou').build()
print(x.to_dict())
