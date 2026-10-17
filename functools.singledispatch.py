# from functools import singledispatch


# @singledispatch
# def display(value):
#     print("unknown value")

# @display.register
# def _(value: int) -> None:
#     print("number:", value)

# @display.register
# def _(value: str) -> None:
#     print("string:", value)

# @display.register
# def _(value: list) ->None:
#     print(f"list with {len(value)} items")


# display(25)
# display("hello")
# display([1, 2, 3])
# display(3.14)