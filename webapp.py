from flask import Flask
from call_api import main as call_api_main

app = Flask(__name__)

@app.route("/")
def index():
    import cProfile
    with cProfile.Profile() as pr:
        # プロファイル対象のコードここから
        call_api_main()
        # プロファイル対象のコードここまで
        # 結果をファイルに保存
        pr.dump_stats("webapp.profile")
    return "Finished"