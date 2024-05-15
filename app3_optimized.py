import datetime
import asyncio
import httpx

url = "http://127.0.0.1:5000/delay/1"


async def main():
    """API呼び出しを10回実行

    httpbinの起動は `gunicorn --threads=10 -b=127.0.0.1:5000 httpbin:app`
    """
    print("start:", datetime.datetime.now())

    requests = []
    async with httpx.AsyncClient() as client:
        for i in range(10):
            requests.append(client.get(url))
        responses = await asyncio.gather(*requests)
    for response in responses:
        print(response.status_code, response.json())

    print("end:", datetime.datetime.now())


if __name__ == "__main__":
    asyncio.run(main())
