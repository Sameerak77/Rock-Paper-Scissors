from flask import Flask,request,render_template
import random
app=Flask(__name__)
@app.route('/')
def ho():
	return render_template("home.html",output=None)
@app.route('/output',methods=['POST'])
def home():
	output=0
	inp=request.form.get('input')
	s=ran()
	if(s==inp):
		output=0
	elif(inp=='rock' and s=='paper'):
		output=0
	elif(inp=='rock' and s=='scissor'):
		output=1
	elif(inp=='scissor' and s=='paper'):
		output=1
	elif(inp=='scissor' and s=='rock'):
		output=0
	elif(inp=='paper' and s=='rock'):
		output=1
	elif(inp=='paper' and s=='scissor'):
		output=1
	ma=[output,s,inp]
	return render_template('home.html',output=ma)
def ran():
	li=['rock','paper','scissor']
	return random.choice(li)
