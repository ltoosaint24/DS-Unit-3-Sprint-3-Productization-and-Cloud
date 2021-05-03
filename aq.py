from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy

APP = Flask(__name__)
@APP.route('/')
def root():
  import openaq
  api = openaq.OpenAQ()
  status, body = api.cities()
  stat = status
  bod = bodies
  results = body['results'][8:10]
  name = 'Chile Los Angelos Data'
  
 
  def get_results(api):
        status, body = api.measurements(city ='Los Angeles',parameter ='pm25')
   
        def create_tup(body):
            tup =()
            tup_list =[]
            for x in body['results']:
      #print(x)
      #print(x['date']['utc'])
      #print(x['value'])
                tup_list.append((x['date']['utc'],x['value']))
            tuples = tup_list
            return tuples
   
        tups =creat_tup(body)
        return tups
    
  los_tup =get_results(api)
  return render_template('index.html',title ="Exploring Flask & Api",  table_title ='Sample Data Results', status = stat, results =results, tuples = los_tups, datalog =name)
  APP.run(host ='0.0.0.0',port =81)