import random
import orjson
from uuid import uuid4

DATA_FILE = "data.jsonl"

nums = list(range(1, 10000001))
random.shuffle(nums)

with open(DATA_FILE, "wb") as output_file:
    for num in nums:
        line = orjson.dumps({"id": num, "value": str(uuid4().hex)})
        output_file.write(line + b"\n")
