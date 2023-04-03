from flask import Flask, request

app = Flask(__name__)

hackathons = {
    "GHW: API Week": {
        "start_date": "2023-04-03 12:00:00",
        "end_date": "2023-04-10 12:00:00",
        "location": "Everywhere, Online",
        "type": "Digital Only"
    },
    "Bitcamp": {
        "start_date": "2023-04-07 12:00:00",
        "end_date": "2023-04-09 12:00:00",
        "location": "College Park, Maryland",
        "type": "In-Person Only"
    }
}

@app.route("/")
def hello_ghw():
	return "<p>Thanks, 404, for all the help!!!</p>"

@app.route('/hackathons', methods=['GET', 'POST'])
def getHackathons():
	if request.method == 'POST':
		hackathons["New Hackathon"] = request.json
		return hackathons
	else:	
		return hackathons

if __name__=="__main__":
	app.run(debug = True)
	

#https://hoppscotch.io/
#https://ghw-logan-api.azurewebsites.net/
#https://portal.azure.com/?Microsoft_Azure_Education_correlationId=0e75ffce4d504be79389307ef337247f&Microsoft_Azure_Education_newA4E=true&Microsoft_Azure_Education_asoSubGuid=d2502a1d-bfc7-4bc4-99b4-af8571a0329e#@pitt.onmicrosoft.com/resource/subscriptions/d2502a1d-bfc7-4bc4-99b4-af8571a0329e/resourceGroups/ghw/providers/Microsoft.Web/sites/ghw-logan-api/appServices
