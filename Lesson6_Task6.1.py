import sys
import argparse


def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('start', nargs='?', type=int)
    parser.add_argument('end', nargs='?', type=int)

    return parser


if __name__ == "__main__":
    parser = createParser()
    namespace = parser.parse_args()
    namespace.start -= 1
    with open('sales.csv', encoding='utf-8') as sales:
        content = sales.readlines()
        content = list(map(lambda s: s.replace('\n', ''), content))
        print(content[namespace.start:namespace.end])
