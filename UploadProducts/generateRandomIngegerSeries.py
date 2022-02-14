from random import randint
import argparse

parser = argparse.ArgumentParser(description="指定要生成序列的长度")
parser.add_argument("seriesLength", type=int, help="指定要生成序列的长度")
args = parser.parse_args()
seriesLength = args.seriesLength


def random_with_N_digits(n):
    range_start = 10 ** (n - 1)
    range_end = (10 ** n) - 1
    return randint(range_start, range_end)


intSeries = random_with_N_digits(seriesLength)
print(intSeries)
