def action(inp, replace_with, move, transition):
    global tapehead, state
    if tape[tapehead] == inp:
        # read
        tape[tapehead] = replace_with  # user string
        state = transition
        if move == "L":
            tapehead -= 1
        else:
            tapehead += 1
        return True
    return False


string = input("Enter string : ")
length = len(string) + 2  # to make counting easier
tape = ["B"] * length  # blank
i = 1
tapehead = 1
# turing machine should quit if there is no change in state

for s in string:
    tape[i] = s
    i += 1

a, b, X, Z, U, V, R, L, B = "a", "b", "X", "Z", "U", "V", "R", "L", "B"
state = 0
oldtapehead = -1
accept = False
while oldtapehead != tapehead:
    oldtapehead = tapehead
    print(tape, "with tapehead at index", tapehead, "on state", state)

    if state == 0:
        if (
            action(a, X, R, 1)
            or action(B, B, R, 10)
            or action(Z, Z, R, 7)
            or action(b, U, R, 4)
        ):
            pass

    elif state == 1:
        if action(a, a, R, 1) or action(b, b, R, 2) or action(B, B, L, 11):
            pass

    elif state == 2:
        if action(b, b, R, 2) or action(Z, Z, R, 2) or action(a, Z, L, 3):
            pass

    elif state == 3:
        if (
            action(b, b, L, 3)
            or action(Z, Z, L, 3)
            or action(a, a, L, 3)
            or action(X, X, R, 0)
        ):
            pass

    elif state == 4:
        if action(b, b, R, 4) or action(Z, Z, R, 5) or action(B, B, L, 15):
            pass

    elif state == 5:
        if action(Z, Z, R, 5) or action(V, V, R, 5) or action(b, V, L, 6):
            pass

    elif state == 6:
        if (
            action(Z, Z, L, 6)
            or action(V, V, L, 6)
            or action(b, b, L, 6)
            or action(U, U, R, 0)
        ):
            pass

    elif state == 7:
        if action(Z, Z, R, 7) or action(V, V, R, 8):
            pass

    elif state == 8:
        if action(V, V, R, 8) or action(B, B, R, 9):
            pass

    elif state == 11:
        if action(a, a, L, 11) or action(X, X, R, 12):
            pass

    elif state == 12:
        if action(a, Z, R, 13):
            pass

    elif state == 13:
        if action(a, X, R, 12) or action(B, B, R, 14):
            pass

    elif state == 15:
        if action(b, b, L, 15) or action(U, U, R, 16):
            pass

    elif state == 16:
        if action(b, V, R, 17):
            pass

    elif state == 17:
        if action(b, U, R, 16) or action(B, B, R, 18):
            pass

    else:
        accept = True


if accept:
    print("String accepted on state = ", state)
else:
    print("String not accepted on state = ", state)
