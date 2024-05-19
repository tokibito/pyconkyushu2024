import datetime
import timeit

DATA_FILE = "data.jsonl"


def main():
    """ファイルの行数をカウントするスクリプト"""
    print("start:", datetime.datetime.now())

    result = 0
    with open(DATA_FILE) as input_file:
        for line in input_file:
            result += 1

    print(f"result: {result} lines")

    print("end:", datetime.datetime.now())


if __name__ == "__main__":
    print(timeit.timeit(main, number=10))
