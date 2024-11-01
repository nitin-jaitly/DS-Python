from collections import deque

def check_matching_parenthesis(s):
    stack = deque()

    for c in s:
        if c == "(":
            stack.append(c)
        elif c == ")":
            if not stack:
                return False
            stack.pop()
    return len(stack) == 0


def main():

    print(check_matching_parenthesis("()"))
    print(check_matching_parenthesis("(hi there )"))
    print(check_matching_parenthesis("(hello) ooo"))
    print(check_matching_parenthesis("((linkedin )) learning"))


    print(check_matching_parenthesis("(hi there ("))
    print(check_matching_parenthesis("() ok )"))
    print(check_matching_parenthesis("((increment)"))
    print(check_matching_parenthesis(")linkedin()("))


if __name__ == "__main__":
    main()