#!/usr/bin/env python3
"""
ASCIICAT - Random ASCII Art Cat Generator
Generates cute random ASCII cats for your terminal!
"""

import random
import sys
import argparse

class ASCIICat:
    def __init__(self):
        self.cats = [
            # Classic sitting cat
            """
     /\\_/\\
    ( o.o )
     > ^ <
            """,

            # Sleeping cat
            """
     /\\_/\\
    ( -.- )
     > ^ <
            """,

            # Happy cat
            """
     /\\_/\\
    ( ^.^ )
     > ^ <
            """,

            # Surprised cat
            """
     /\\_/\\
    ( O.O )
     > ^ <
            """,

            # Big cat
            """
      /\\___/\\
     (  o   o  )
      )  L  (
     (   v   )
    ^^m^^^^^^m^^
            """,

            # Small cat
            """
   /\\_/\\
  ( o.o )
   > ^ <
            """,

            # Cat with tongue out
            """
     /\\_/\\
    ( o.o )
     >:P <
            """,

            # Cat looking sideways
            """
     /\\_/\\
    ( -.o )
     > ^ <
            """,

            # Chubby cat
            """
      /\\___/\\
     (  o   o  )
    (     U     )
     \\  ___  /
      \\_____/
            """,

            # Minimalist cat
            """
   /\\_/\\
  ( . .)
   )___(
            """
        ]

        self.colors = {
            'reset': '\033[0m',
            'black': '\033[30m',
            'red': '\033[31m',
            'green': '\033[32m',
            'yellow': '\033[33m',
            'blue': '\033[34m',
            'magenta': '\033[35m',
            'cyan': '\033[36m',
            'white': '\033[37m',
            'bright_black': '\033[90m',
            'bright_red': '\033[91m',
            'bright_green': '\033[92m',
            'bright_yellow': '\033[93m',
            'bright_blue': '\033[94m',
            'bright_magenta': '\033[95m',
            'bright_cyan': '\033[96m',
            'bright_white': '\033[97m'
        }

    def get_random_cat(self, colored=False):
        """Returns a random ASCII cat"""
        cat = random.choice(self.cats)

        if colored:
            color = random.choice(list(self.colors.keys())[1:-1])  # Exclude reset
            return self.colors[color] + cat + self.colors['reset']

        return cat

    def meow(self):
        """Returns a random meow sound"""
        meows = [
            "Meow!", "Miau!", "Mrow!", "Purr...",
            "Mew mew!", "Nya~", "Prrrr", "*purr*"
        ]
        return random.choice(meows)

def main():
    parser = argparse.ArgumentParser(description='Generate random ASCII cats!')
    parser.add_argument('-c', '--color', action='store_true',
                       help='Add random colors to the cat')
    parser.add_argument('-m', '--meow', action='store_true',
                       help='Add a random meow sound')
    parser.add_argument('-n', '--number', type=int, default=1,
                       help='Number of cats to generate (default: 1)')

    args = parser.parse_args()

    cat_generator = ASCIICat()

    for i in range(args.number):
        if i > 0:
            print()  # Space between cats

        cat = cat_generator.get_random_cat(colored=args.color)
        print(cat)

        if args.meow:
            print(f"    {cat_generator.meow()}")

if __name__ == "__main__":
    main()