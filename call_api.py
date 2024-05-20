import datetime
import httpx

url = "http://127.0.0.1:5000/delay/1"


def main():
    """API呼び出しを10回実行
    """
    print("start:", datetime.datetime.now())

    for i in range(10):
        response = httpx.get(url)
        print(response.status_code, response.json())

    print("end:", datetime.datetime.now())


if __name__ == "__main__":
    main()
