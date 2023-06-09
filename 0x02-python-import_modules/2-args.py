#!/usr/bin/python3
if __name__ == "__main__":

    import sys

    args = sys.argv[1:]
    nb_args = len(args)

    if nb_args == 0:
        print("0 arguments.")
    elif nb_args == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(nb_args))

    for i in range(nb_args):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
