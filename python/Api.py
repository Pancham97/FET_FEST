import flask as flask
import json, csv
import app as app
import app2 as app2

input = {
	'input' : [
		'sym1', 
		'sym2'
	]
}

jsoninput = json.dumps(input)




f = open( 'DiseaseList.csv', 'r' )
csvReader = csv.DictReader(f, ['Disease'])
output = json.dumps( [ row for row in csvReader ] )

#config your server data
app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/api/getkeys', methods=['GET'])
def getKeys():
	
	print (inputjson)
	return output

@app.route('/api/getdata', methods=['GET', 'POST'])
def getData():
	inputjson = request.json
	
	output = app.findMatchingDiseases(inputjson)
	return output
	
app.run()