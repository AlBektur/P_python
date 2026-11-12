#!/opt/pyenv/shims/python

import sys

if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    if len(sys.argv) > 1:
        arguments = sys.argv[1:]
        i:int = 0
        flag:int = 0
        summa: int = 0

        min_val: int = arguments[0]
        max_val: int = arguments[0]


        arguments = [int(x) for x in arguments]
            
        while i < len(arguments):
            summa += arguments[i]
            if max_val < arguments[i]:
                max_val = arguments[i]
            if min_val > arguments[i]:
                min_val = arguments[i]
            i += 1
        if flag:
            pass
        else:
            print(f"Scores processed: {arguments}")
            print(f"Total players: {len(arguments)}")
            print(f"Total score: {summa}")
            print(f"Average score: {summa / len(arguments)}")
            print(f"High score: {max_val}")
            print(f"Low score: {min_val}")
            print(f"Score range: {int(max_val) - int(min_val)}")
    else:
        print(
            "No scores provided. Usage: "
            "python3 ft_score_analytics.py <score1> <score2> ..."
            )
