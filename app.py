from flask import Flask
from flask import render_template
from flask import request
import pickle 
app = Flask(__name__)

@app.route('/')
def hello():
      return render_template('index.html')
if request:

     EstimatedSalary= request.form['EstimatedSalary']
     print('EstimatedSalary')
     purchased= model.predict([[float(EstimatedSalary)]])
     print(purchased[0])
     model= pickle.load(open('model.pkl','rb'))
  
@app.route('/prediction')
def predict():
      return render_template('prediction.html')
if __name__=='__main__':
    app.run()