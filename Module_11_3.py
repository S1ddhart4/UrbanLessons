def introspection_info(obj):

    info = {}

    info['type'] = type(obj).__name__

    info['attributes'] = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith('__')]

    info['methods'] = [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith('__')]

    info['module'] = getattr(obj, '__module__', 'built-in')

    if hasattr(obj, '__doc__'):
        info['doc'] = obj.__doc__

    return info

class ExampleClass:

    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, {self.name}!"

example_obj = ExampleClass("Alice")

example_info = introspection_info(example_obj)

print(example_info)

number_info = introspection_info(42)
print(number_info)