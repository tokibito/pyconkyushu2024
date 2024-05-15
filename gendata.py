import random
import json
from uuid import uuid4

nums = list(range(1, 10000001))
random.shuffle(nums)

for num in nums:
    line = json.dumps({"id": num, "value": str(uuid4().hex)})
    print(line)
