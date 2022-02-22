import sys
import argparse


def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('sum', nargs='?', default='0')
    #parser.add_argument('--sum', nargs='?', default='0')

    return parser


if __name__ == "__main__":
    parser = createParser()
    namespace = parser.parse_args()

    with open('sales.csv', 'a', encoding='utf-8') as sales:
        sales.write("{} \n".format(namespace.sum))


