#!/usr/bin/python2
# Simple example of batch program. Takes a file as argv.
import sys
import time


def do_job():
    if len(sys.argv) != 2:
        raise AttributeError
    numbers = []
    with open(sys.argv[1]) as f:
        for line in f:
            numbers.append(float(line))
    powers = [x**2 for x in numbers]

    time.sleep(10)

    with open("powers", "w") as f:
        for a, b in zip(numbers, powers):
            f.write("{}^2={}".format(a, b))
            f.write("\n")


if __name__ == "__main__":
    do_job()
    print "elo job"
