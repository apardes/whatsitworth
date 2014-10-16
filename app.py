import json
import urllib
from flask import Flask, render_template, request
from re import sub
from decimal import Decimal
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/search', methods = ['POST'])
def search():
	query = request.form['query']
	print "\n{}".format(query)

	prices = ebayQuery(query)

	final = calculate(prices)

	avg = round(final['average'], 2)
	low = round(final['low'], 2)
	high = round(final['high'], 2)

	return render_template('results.html', average = avg, low = low, high = high, query = query)


def calculate(json):
	data = json
	i = 0
	total = 0
	high = 0
	low = 0
	for x in data["results"]['collection1']:
		val = x['sold_price']
		#val = val.strip('$')
		if "to" in val:
			pass
		else:
			value = Decimal(sub(r'[^\d.]', '', val))
			if value < 20:
				pass
			else:
				total += value
				if value > high:
					high = value
				else:
					pass
				if value < low:
					low = value
				else:
					pass
				i += 1

		print value

	avg = total / i

	answer = {'average' : avg, 'low' : low, 'high' : high}

	print i
	print total
	return answer


def ebayQuery(query):
	query = str(query)

	query_url = "https://www.kimonolabs.com/api/3w30t26k?apikey=097be8f885a1cf8bbe7509f5574a461e"

	parameter = "&_nkw="

	safe_query = urllib.quote(query)

	final_query = query_url + parameter + safe_query
	print final_query

	results = json.load(urllib.urlopen(final_query))

	return results

if __name__ == '__main__':
    app.run()