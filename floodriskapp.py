#!/usr/bin/python3

# -*- coding: utf-8 -*-
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#	  http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import json
import os
import requests
from dotenv import load_dotenv
from flask import Flask, request, session, render_template, flash
from requests.auth import HTTPBasicAuth

app = Flask(__name__)

app.config.update(dict(
	DEBUG=True,
	SECRET_KEY=os.environ.get('SECRET_KEY', 'development key')
))

#strings = {
#"GEOIDX": ["X220710001002", "X220710002002", "X220710003001", "X220710003002", "X220710004001", "X220710004002", "X220710006011", "X220710006012", "X220710006021", "X220710006022", "X220710006023", "X220710006031", "X220710006032", "X220710006041", "X220710006042", "X220710006043", "X220710006051", "X220710006052", "X220710006053", "X220710006061", "X220710006062", "X220710006063", "X220710006071", "X220710006072", "X220710006073", "X220710006111", "X220710006112", "X220710006131", "X220710006132", "X220710006133", "X220710006151", "X220710006152", "X220710006161", "X220710006162", "X220710006163", "X220710006171", "X220710006172", "X220710006181", "X220710006182", "X220710007011", "X220710007012", "X220710007013", "X220710007014", "X220710007021", "X220710007022", "X220710007023", "X220710007024", "X220710008001", "X220710008002", "X220710008003", "X220710009011", "X220710009012", "X220710009013", "X220710009014", "X220710009021", "X220710009022", "X220710009023", "X220710009024", "X220710009031", "X220710009032", "X220710009033", "X220710009034", "X220710009041", "X220710009042", "X220710011001", "X220710011002", "X220710012001", "X220710012002", "X220710013011", "X220710013012", "X220710013013", "X220710013014", "X220710013021", "X220710013022", "X220710014011", "X220710014012", "X220710014013", "X220710014014", "X220710014015", "X220710014016", "X220710014021", "X220710014022", "X220710014023", "X220710014024", "X220710015001", "X220710015002", "X220710017011", "X220710017012", "X220710017013", "X220710017021", "X220710017022", "X220710017023", "X220710017024", "X220710017201", "X220710017202", "X220710017203", "X220710017204", "X220710017221", "X220710017222", "X220710017223", "X220710017224", "X220710017225", "X220710017226", "X220710017227", "X220710017231", "X220710017232", "X220710017233", "X220710017234", "X220710017241", "X220710017242", "X220710017243", "X220710017244", "X220710017251", "X220710017252", "X220710017253", "X220710017254", "X220710017301", "X220710017341", "X220710017351", "X220710017352", "X220710017361", "X220710017362", "X220710017371", "X220710017372", "X220710017373", "X220710017391", "X220710017392", "X220710017401", "X220710017402", "X220710017403", "X220710017411", "X220710017431", "X220710017432", "X220710017441", "X220710017442", "X220710017451", "X220710017452", "X220710017461", "X220710017462", "X220710017463", "X220710017471", "X220710017472", "X220710017481", "X220710017482", "X220710017483", "X220710017484", "X220710017491", "X220710017501", "X220710017503", "X220710017511", "X220710018001", "X220710018002", "X220710019001", "X220710019002", "X220710020001", "X220710020002", "X220710020003", "X220710021001", "X220710021002", "X220710022001", "X220710022002", "X220710022003", "X220710023001", "X220710023002", "X220710023003", "X220710023004", "X220710023005", "X220710024011", "X220710024012", "X220710024021", "X220710024022", "X220710024023", "X220710024024", "X220710025011", "X220710025012", "X220710025013", "X220710025014", "X220710025021", "X220710025022", "X220710025023", "X220710025024", "X220710025031", "X220710025032", "X220710025033", "X220710025041", "X220710025042", "X220710025043", "X220710025044", "X220710026001", "X220710027001", "X220710027002", "X220710028001", "X220710028003", "X220710029001", "X220710029003", "X220710030001", "X220710030002", "X220710031001", "X220710031002", "X220710033011", "X220710033012", "X220710033013", "X220710033021", "X220710033022", "X220710033023", "X220710033024", "X220710033031", "X220710033033", "X220710033041", "X220710033042", "X220710033071", "X220710033072", "X220710033081", "X220710033082", "X220710033083", "X220710033084", "X220710033085", "X220710033086", "X220710034001", "X220710034002", "X220710035002", "X220710035003", "X220710036001", "X220710036002", "X220710036003", "X220710037011", "X220710037012", "X220710037021", "X220710037022", "X220710037023", "X220710037024", "X220710037025", "X220710037026", "X220710039002", "X220710040001", "X220710040002", "X220710041001", "X220710041002", "X220710044011", "X220710044012", "X220710044013", "X220710044022", "X220710045001", "X220710045002", "X220710045003", "X220710046001", "X220710046002", "X220710046003", "X220710049001", "X220710049002", "X220710049003", "X220710049004", "X220710050001", "X220710050002", "X220710054001", "X220710054002", "X220710054003", "X220710055001", "X220710055002", "X220710055003", "X220710056011", "X220710056012", "X220710056013", "X220710056014", "X220710056021", "X220710056022", "X220710056023", "X220710056024", "X220710056031", "X220710056032", "X220710056033", "X220710056041", "X220710056042", "X220710056043", "X220710060001", "X220710063001", "X220710063002", "X220710063003", "X220710064001", "X220710064002", "X220710064003", "X220710064004", "X220710065001", "X220710065002", "X220710065003", "X220710069001", "X220710069002", "X220710070001", "X220710070002", "X220710071011", "X220710071012", "X220710072001", "X220710072002", "X220710072003", "X220710075011", "X220710075012", "X220710075013", "X220710075014", "X220710075015", "X220710075021", "X220710075022", "X220710075023", "X220710075024", "X220710075025", "X220710076041", "X220710076042", "X220710076051", "X220710076052", "X220710076061", "X220710076062", "X220710076063", "X220710077001", "X220710077002", "X220710078001", "X220710082001", "X220710082002", "X220710083001", "X220710083002", "X220710084001", "X220710084002", "X220710085001", "X220710086001", "X220710088001", "X220710088002", "X220710090001", "X220710090002", "X220710090003", "X220710092001", "X220710092002", "X220710092003", "X220710094001", "X220710094002", "X220710094003", "X220710094004", "X220710097001", "X220710099001", "X220710099003", "X220710100001", "X220710100003", "X220710100004", "X220710101001", "X220710101002", "X220710102001", "X220710102002", "X220710102003", "X220710102004", "X220710102005", "X220710103001", "X220710103002", "X220710103003", "X220710103004", "X220710106002", "X220710107001", "X220710107002", "X220710108001", "X220710108002", "X220710109001", "X220710109002", "X220710109003", "X220710109004", "X220710111001", "X220710111002", "X220710111003", "X220710112001", "X220710112002", "X220710114001", "X220710114002", "X220710115001", "X220710115002", "X220710116001", "X220710116002", "X220710117001", "X220710117002", "X220710117003", "X220710117004", "X220710119001", "X220710119002", "X220710119003", "X220710120001", "X220710120002", "X220710121011", "X220710121012", "X220710121021", "X220710121022", "X220710121023", "X220710122001", "X220710122002", "X220710123001", "X220710123002", "X220710123003", "X220710124001", "X220710124002", "X220710125001", "X220710125002", "X220710126001", "X220710126002", "X220710126003", "X220710127001", "X220710127002", "X220710127003", "X220710127004", "X220710128001", "X220710128002", "X220710128003", "X220710129001", "X220710129002", "X220710130001", "X220710130002", "X220710130003", "X220710131001", "X220710131002", "X220710132001", "X220710132002", "X220710132003", "X220710132004", "X220710133011", "X220710133012", "X220710133013", "X220710133014", "X220710133021", "X220710133022", "X220710134003", "X220710136001", "X220710136002", "X220710137001", "X220710137002", "X220710137004", "X220710138001", "X220710138003", "X220710139001", "X220710139002", "X220710140003", "X220710140004", "X220710141001", "X220710142001", "X220710142002", "X220710142003", "X220710143002", "X220710143003", "X220710144001", "X220710144002", "X220710144003", "X220710145001", "X220719801001"]
#}

# min, max, default value
floats = {
	"LOG_ALAND":[4.849075282, 8.081858542, 5.455002938], 
	"LOG_AWATER":[0, 7.906871635, 0.915597473],
	"VACANT_PERC":[0, 1, 0.16], 
	"LOTTOTACRES":[11.6, 15997, 149], 
	"LOTAVEACRES":[0.07, 29.9, 0.36472973], 
	"LOTSTDEV":[0.03, 371.21, 2.188716216], 
	"LOT/BLK":[0.6, 107.6, 19.81846847], 
	"ROAD/LOT":[0, 5.41, 0.488603604], 
	"TREE/ACRE":[0.06, 4862564.35, 16082.0534], 
	"BLKGRPACRES":[17.45648562, 29835.96402, 225.9353933], 
	"ROADAREAACRES":[0.14678037, 15598.86316, 94.27037273]
}

# min, max, default value
ints = {
	"STRUCTURE":[0, 757, 242],
	"SLAB":[0, 737, 102], 
	"CRAWLSP":[0, 375, 129], 
	"RAISED":[0, 369, 11], 
	"FREEBRD":[0, 379, 25], 
	"RLPROP":[1, 244, 14], 
	"CLAIMSTL":[2, 821, 54], 
	"AVECLAIMS":[2, 11, 3],  
	"LOTCNT":[9, 3013, 312], 
	"GRADEDLOTS":[6, 1240, 291], 
	"VACANT":[0, 750, 50], 
	"BLKCOUNT":[1, 144, 17], 
	"TREECNT":[0, 2000, 217], 
	"HISTZONE":[1, 7, 3]
}

labels = ["Low_Risk", "High_Risk"]


def generate_input_lines():
	result = f'<table>'

	counter = 0
	for k in floats.keys():
		minn, maxx, vall = floats[k]
		if (counter % 2 == 0):
			result += f'<tr>'
		result += f'<td>{k}'
		result += f'<input type="number" class="form-control" min="{minn}" max="{maxx}" step="1" name="{k}" id="{k}" value="{vall}" required (this.value)">'
		result += f'</td>'
		if (counter % 2 == 1):
			result += f'</tr>'
		counter = counter + 1

	counter = 0
	for k in ints.keys():
		minn, maxx, vall = ints[k]
		if (counter % 2 == 0):
			result += f'<tr>'
		result += f'<td>{k}'
		result += f'<input type="number" class="form-control" min="{minn}" max="{maxx}" step="1" name="{k}" id="{k}" value="{vall}" required (this.value)">'
		result += f'</td>'
		if (counter % 2 == 1):
			result += f'</tr>'
		counter = counter + 1

	"""
	counter = 0
	for k in strings.keys():
		if (counter % 2 == 0):
			result += f'<tr>'
		result += f'<td>{k}'
		result += f'<select class="form-control" name="{k}">'
		for value in strings[k]:
			result += f'<option value="{value}" selected>{value}</option>'
		result += f'</select>'
		result += f'</td>'
		if (counter % 2 == 1):
			result += f'</tr>'
		counter = counter + 1
	"""

	result += f'</table>'

	return result


app.jinja_env.globals.update(generate_input_lines=generate_input_lines)


def get_token():
	auth_token = os.environ.get('AUTH_TOKEN')
	api_token = os.environ.get("API_TOKEN")
	token_request_url = os.environ.get("TOKEN_REQUEST_URL")

	if (auth_token):
		# All three are set. bad bad!
		if (api_token and auth_token):
			raise EnvironmentError('[ENV VARIABLES] please set either "AUTH_TOKEN" or "API_TOKEN". Not both.')
		# Only TOKEN is set. good.
		else:
			return auth_token
	else:
		# Nothing is set. bad!
		if not (api_token and token_request_url):
			raise EnvironmentError('[ENV VARIABLES] Please set "API_TOKEN" as "AUTH_TOKEN" is not set.')
		# Only USERNAME, PASSWORD are set. good.
		else:
			token_response = requests.post(token_request_url, data={"apikey": api_token, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
			if token_response.status_code == 200:
				return token_response.json()["access_token"]
			else:
				raise Exception(f"Authentication returned {token_response.status_code}: {token_response.text}")


class riskForm():

	@app.route('/', methods=['GET', 'POST'])
	def index():

		if request.method == 'POST':
			ID = 999

			session['ID'] = ID
			data = {}

			for k, v in request.form.items():
				data[k] = v
				session[k] = v

			scoring_href = os.environ.get('MODEL_URL')

			if not (scoring_href):
				raise EnvironmentError('[ENV VARIABLES] Please set "URL".')

			for field in ints.keys():
				data[field] = int(data[field])
			for field in floats.keys():
				data[field] = float(data[field])

			input_data = list(data.keys())
			input_values = list(data.values())

			payload_scoring = {"input_data": [
				{"fields": input_data, "values": [input_values]}
			]}
			print("Payload is: ")
			print(payload_scoring)
			header_online = {
				'Cache-Control': 'no-cache',
				'Content-Type': 'application/json',
				'Authorization': 'Bearer ' + get_token()
			}
			response_scoring = requests.post(
				scoring_href,
				verify=True,
				json=payload_scoring,
				headers=header_online)
			
			result = response_scoring.text
			print("Result is ", result)
			
			result_json = json.loads(result)
			print(result_json)

			result_keys = result_json['predictions'][0]['fields']
			result_vals = result_json['predictions'][0]['values']

			result_dict = dict(zip(result_keys, result_vals[0]))

			flood_risk = ''
			if "predictedLabel" in result_dict:
				loan_risk = result_dict["predictedLabel"].lower()
			if "prediction" in result_dict:
				loan_risk = result_dict["prediction"].lower()

			no_percent = result_dict["probability"][0] * 100
			yes_percent = result_dict["probability"][1] * 100
			flash('Percentage of this Property being at flood risk is: %.0f%%'
				% yes_percent)
			return render_template(
				'score.html',
				result=result_dict,
				loan_risk=flood_risk,
				yes_percent=yes_percent,
				no_percent=no_percent,
				response_scoring=response_scoring,
				labels=labels)

		else:
			return render_template('input.html')


load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))
port = os.environ.get('PORT', '5000')
host = os.environ.get('HOST', '0.0.0.0')
if __name__ == "__main__":
	app.run(host=host, port=int(port))
