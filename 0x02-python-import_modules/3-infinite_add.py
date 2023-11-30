#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    summ = 0
    arguments = sys.argv[1:]
    for arg in arguments:
        summ += int(arg)
    print(f"{summ}")
