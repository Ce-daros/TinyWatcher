import util
from flask import Flask

app = Flask(__name__)


@app.route('/cpu')
def cpu():
    return str(util.get_CPU_usage())


@app.route('/ram_total')
def ram_total():
    return str(util.get_RAM(1)[0])


@app.route('/ram_used')
def ram_used():
    return str(util.get_RAM(1)[1])


@app.route('/ram_free')
def ram_free():
    return str(util.get_RAM(1)[2])


@app.route('/all')
def all():

    return str(f"""
    CPU Usage { util.get_CPU_usage() }%<br>
    RAM Total { util.get_RAM()[0] } Used { util.get_RAM()[1] }<br>
    Disk Read { util.get_DiskIO()[0] } Write { util.get_DiskIO()[1] }<br>
    Network Read { util.get_NetIO()[0] } Write { util.get_NetIO()[1] }
    """)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
