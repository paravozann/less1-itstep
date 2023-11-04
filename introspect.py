# import inspect
# import requests
# import sys
# print(sys.executable)
# print(sys
# print(inspect.ismodule(requests))
# print(inspect.isclass(requests.Session))
# print(inspect.isfunction(requests.get))

# data = "string"
#
# def fun():
#     pass
#
# startLetter = input("Input first letter:")
#
#
# for method in dir(data):
#     if method.startswith(startLetter.lower()):
#          print(method)

# data = "string"
# print(getattr(data, "reverse", None))
# print(getattr(data, "index", None))
# print("callable data - ", callable(data))
# print("callable data - ", callable(fun))
#
#
# class Parent:
#     pass
#
# class Child(Parent):
#     pass
#
# print(issubclass(Parent , Child))
# print(issubclass(Child, Parent))
# petr = Parent()
# petrPetrivich = Child()
#
# print(isinstance(petr, Parent))
# print(isinstance(petrPetrivich, Child))
