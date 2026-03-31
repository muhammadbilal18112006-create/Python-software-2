# QUESTION NO 1

from flask import Flask, jsonify

app = Flask(__name__)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

@app.route("/prime_number/<int:number>")
def prime_number(number):
    result = {
        "Number": number,
        "isPrime": is_prime(number)
    }
    return jsonify(result)

if __name__ == "__main__":
    app.run()


# QUESTION NO 2

from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

def get_airport_info(icao):
    conn = sqlite3.connect("airports.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name, municipality FROM airport WHERE ident = ?", (icao,))
    result = cursor.fetchone()
    conn.close()
    return result


@app.route("/airport/<string:icao>")
def airport(icao):
    data = get_airport_info(icao)

    if data:
        name, city = data
        return jsonify({
            "ICAO": icao,
            "Name": name,
            "Location": city
        })
    else:
        return jsonify({"error": "Airport not found"}), 404


if __name__ == "__main__":
    app.run(use_reloader=False)
