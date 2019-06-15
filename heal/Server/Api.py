import flask as flask
import json, csv


f = open( 'DiseaseList.csv', 'r' )
csvReader = csv.DictReader(f, ['Disease'])
output = json.dumps( [ row for row in csvReader ] )

#config your server data
app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/api/getkeys', methods=['GET'])
def getKeys():
	return output

@app.route('/api/getdata', methods=['GET'])
def getData():
	return output
	
app.run()