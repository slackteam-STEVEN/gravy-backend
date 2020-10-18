from flask import Flask
from flask import request
from flask import jsonify
from get_db_channel_data import channel_data
from get_db_video_data import video_data

app = Flask(__name__)

@app.route("/")
def top():
    return "test"

@app.route("/video", methods=["POST"])
def video():
    end_created_at = request.form["end_created_at"]
    start_created_at = request.form["start_created_at"]
    category = request.form["category"]
    video_data_result = video_data(end_created_at, start_created_at, category)

    return jsonify(video_data_result)


@app.route("/channel", methods=["POST"])
def channel():
    end_created_at = request.form["end_created_at"]
    start_created_at = request.form["start_created_at"]
    channel_data_result = channel_data(end_created_at, start_created_at)

   # created_at = request.form["channel_data"]
    return jsonify(channel_data_result)
    # return channel_data_result

    # メイン関数
    # メイン関数とは、Pythonを実行した際、最初に呼ばれる関数
if __name__ == "__main__":
    app.run(debug=True)