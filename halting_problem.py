# feed the decider to itself, it loops : so undecidable problems do exist.
# if its true : terminate and give result, but if i'ts a bad function it says false

def hold(fun, arg):
    pass

def decider(fun):
    if holds(fun, fun):
        while true:
            pass
    else:
        return

decider_text =
"""
def decider(fun):
    if holds(fun, fun):
        while true:
            pass
    else:
        return

"""

decider(decider_text)
