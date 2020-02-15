from flask import Flask, render_template, request

import data_manager as dmg

app = Flask('__main__')


@app.route("/", methods=['GET', 'POST'])
def home():

    return render_template('home.html')


@app.route("/request-counter", methods=["GET", "POST", "PUT", "DELETE"])
def counter():

    GET = 0
    POST = 1
    PUT = 2
    DELETE = 3
    all_stats = dmg.read_stats_from_file()

    counters = {
        "GET":  int(all_stats[GET][-1]),
        "POST": int(all_stats[POST][-1]),
        "PUT": int(all_stats[PUT][-1]),
        "DELETE": int(all_stats[DELETE][-1])
    }

    if request.method == "GET":
        counters['GET'] += 1
    elif request.method == "POST":
        counters['POST'] += 1
    elif request.method == "DELETE":
        counters['DELETE'] += 1
    elif request.method == "PUT":
        counters['PUT'] += 1

    dmg.write_stats_to_file(counters)
    return render_template("request-counter.html")


@app.route("/statistics")
def statistics():

    TABLE_HEADERS = ["Method", "Count"]
    all_stats = dmg.read_stats_from_file()

    return render_template("statistics.html", all_stats=all_stats, TABLE_HEADERS=TABLE_HEADERS)


if __name__ == "__main__":
    app.run(
        port=5000,
        debug=True
    )
