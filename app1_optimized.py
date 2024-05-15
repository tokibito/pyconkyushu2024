import datetime
import timeit

DATA_FILE = "data.jsonl"


def main():
    """ファイルの行数をカウントするスクリプト
    """
    print("start:", datetime.datetime.now())

    result = 0
    with open(DATA_FILE, "rb") as input_file:
        data = input_file.read()
        result = data.count(b"\n")

    print(f"result: {result} lines")

    print("end:", datetime.datetime.now())


if __name__ == "__main__":
    print(timeit.timeit(main, number=10))
