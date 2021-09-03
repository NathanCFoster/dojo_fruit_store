from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    charge = int(request.form['strawberry']) + int(request.form['raspberry']) + int(request.form['apple'])
    print("Charging %s for %d fruits" %(request.form['first_name'], charge))
    name = request.form['first_name']
    lastName = request.form['last_name']
    studentID = request.form['student_id']
    strawberry = request.form['strawberry']
    raspberry = request.form['raspberry']
    apple = request.form['apple']
    return redirect('/realcheckout/%s/%s/%s/%s/%s/%s' %(name, lastName, studentID, strawberry, raspberry, apple))

@app.route("/realcheckout/<name>/<lastName>/<studentID>/<strawberry>/<raspberry>/<apple>", methods=['Get'])
def checkedOut(name, lastName, studentID, strawberry, raspberry, apple):
    return render_template("checkout.html", name=name, lastName=lastName, studentID=studentID, strawberry=strawberry, raspberry=raspberry, apple=apple)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    
