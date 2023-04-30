import numpy as np 
from flask import Flask,request,jsonify,render_template
import pickle


app=Flask(__name__)

model=pickle.load(open("modelfile.pkl","rb"))

@app.route("/")
def home():
	return render_template("index.html")

		# male -   0 1
		#female -  1 0

@app.route("/predict",methods=["POST"])
def predict():
	if request.method=="POST":
		check=[]
		gender=request.form['Gender']
		if gender == 'male':
			check.append(0);
			check.append(1);

		if gender =='female':
			check.append(1);
			check.append(0);


		# check.append(0)
		# check.append(1)
		age=request.form['Age']
		check.append(float(age))
		height=request.form['Height']
		check.append(float(height))
		weight=request.form['Weight']
		check.append(float(weight))
		duration=request.form['Duration']
		check.append(float(duration))
		heart_rate=request.form['Heart_rate']
		check.append(float(heart_rate))
		body_temp=request.form['Body_temperature']
		check.append(float(body_temp))

		print("\t\t\t\t\t\t\t\t\t\tCheck :  ",check)

		prediction=float(model.predict([check]))


		return render_template('index.html',pt=f'{prediction}')
		





if __name__=="__main__":
	app.run(debug=True)
