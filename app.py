from flask import Flask
import os
import datetime
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    name = "Your Full Name"
    username = os.getlogin()
    ist_time = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=5, minutes=30)))
    ist_time_str = ist_time.strftime("%Y-%m-%d %H:%M:%S %Z%z")
    top_output = subprocess.getoutput("top -b -n 1")

    return f"""
    <h2>Name: {name}</h2>
    <h3>Username: {username}</h3>
    <h3>Server Time in IST: {ist_time_str}</h3>
    <pre>{top_output}</pre>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
