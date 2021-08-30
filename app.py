#Importing all Modules Required
import numpy as np
from flask import Flask, render_template, request, jsonify
import pickle
import pygal
from pygal.style import NeonStyle

#Initializing our application
app=Flask(__name__)

#Loading all the dumped .pkl files
model=pickle.load(open('/home/co2analysis/mysite/model.pkl','rb'))
arr1=pickle.load(open('/home/co2analysis/mysite/array1.pkl','rb'))
arr2=pickle.load(open('/home/co2analysis/mysite/array2.pkl','rb'))
newarr=pickle.load(open('/home/co2analysis/mysite/co2_compare.pkl','rb'))

#Creating home page of co2analysis.pythonanywhere.com
@app.route('/', methods=['GET','POST'])
def home():
    return render_template('index.html')

#Redirecting to co2analysis.pythonanywhere.com/dataset
@app.route('/dataset')
def chart():
    #Creating Interactive Scatter Chart using pygal Module
    dot_chart = pygal.XY(stroke=False, height=400, style=NeonStyle)
    dot_chart.title = 'CO2 Emission From Vehicles'
    dot_chart.add('Weight of Vehicle : CO2 Emission', arr1, dots_size=6)
    dot_chart.add('Volume of Engine : CO2 Emission', arr2, dots_size=6)
    graph_data = dot_chart.render_data_uri()
    return render_template("dataset.html", graph_data = graph_data)

#Redirecting to co2analysis.pythonanywhere.com/compare
@app.route('/compare')
def barchart():
    #Creating Interactive Bar Chart using pygal Module
    try:
        line_chart = pygal.Bar(height=400, style=NeonStyle)
        line_chart.title = 'Comparison of CO2 Emission'
        line_chart.x_labels = ['CO2 Emission(g/km)']
        line_chart.add('Audi', newarr[0])
        line_chart.add('BMW',newarr[1])
        line_chart.add('Ford',newarr[2])
        line_chart.add('Honda',newarr[3])
        line_chart.add('Mercedes-Benz',newarr[4])
        line_chart.add('Toyota',newarr[5])
        graph_data1=line_chart.render_data_uri()
        return render_template("compare.html", graph_data1 = graph_data1)
    except Exception as e:
        return str(e)

#Redirecting to co2analysis.pythonanywhere.com/predict
@app.route('/predict', methods=['POST'])
def predict():
    #Taking Inputs from WebPage and Giving Output using POST method
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    output = round(prediction[0], 2)
    return render_template('index.html', prediction_text='CO2 Emission of the vehicle is : {}g/Km'.format(output))

@app.route('/predict_api', methods=['POST'])
def predict_api():
    data=request.get_json(force=True)
    prediction=model.predict([np.array(list(data.values))])
    output=prediction[0]
    return jsonify(output)

if __name__=="__main__":
    app.run(debug=True)