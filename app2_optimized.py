import orjson
import datetime

DATA_FILE = "data.jsonl"


def main():
    """ファイル内のUUIDに重複がないか検証するスクリプト
    """
    print("start:", datetime.datetime.now())

    uuids = set()
    with open(DATA_FILE) as input_file:
        records = input_file.read().splitlines()
    print("read file finished.")
    for line in records:
        data = orjson.loads(line)
        value = data["value"]
        if value in uuids:
            print(f"UUIDの重複が見つかりました: {line}")
            break
        uuids.add(value)

    print("end:", datetime.datetime.now())


if __name__ == "__main__":
    main()
