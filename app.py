from flask import Flask, jsonify, request
from datetime import datetime

current_date = datetime.today()
app = Flask(__name__)

@app.route('/api')
def hello_world():
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')

    current_weekday = current_date.strftime('%A')

    now = datetime.utcnow()
    utc_time = now.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')

    return jsonify({
                "slack_name": slack_name,
                "current_day": current_weekday,
                "utc_time": utc_time,
                "track": track,
                "github_file_url": "https://github.com/NattyGold/HNG-Create-Endpoint-Api-Deploy-Stage1/blob/master/app.py",
                "github_repo_url": "https://github.com/NattyGold/HNG_Create-End-Point-API-Deploy-Stage1",
                "status_code": 200
     })


if __name__=='__main__':
    app.run()


# code by nattygold