import os
import sys
import time


class cursor:
    def spinning_cursor():
        while True:
            for cursor in "|/-\\":
                yield cursor

    global spinner
    spinner = spinning_cursor()

    def Spinner(delay):
        for _ in range(20):
            sys.stdout.write(next(spinner))

            sys.stdout.flush()
            """Calling sys.stdout.flush() forces it to "flush"
            the buffer, meaning that it will write everything
            in the buffer to the terminal, even if normally it
            would wait before doing so."""

            time.sleep(delay)
            sys.stdout.write("\b")
        sys.stdout.write(" ")


class style:
    def print(str, delay):
        for letter in str:
            sys.stdout.write(letter)
            sys.stdout.flush()
            time.sleep(delay)

    def newLine():
        sys.stdout.write("\n")
