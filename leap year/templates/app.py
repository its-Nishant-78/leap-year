from flask import Flask, render_template, request
from datetime import date

app=Flask(__name__)

@app.route("/",methods=['POST','GET'])
def calculate():
    difference=None
    if request.method == 'POST':
        date1 = int(request.form.get('date1',0))
        date2 = int(request.form.get('date2',0))
        month1 = int(request.form.get('month1',0))
        month2 = int(request.form.get('month2',0)) 
        year1 = int(request.form.get('year1',0)) 
        year2 = int(request.form.get('year2',0))
        n1 = date(year1, month1, date1)
        n2 = date(year2, month2, date2)
        difference = (n2 - n1).days
    return render_template('index.html',difference=difference)

if __name__ == "__main__":
    app.run(debug=True)
    