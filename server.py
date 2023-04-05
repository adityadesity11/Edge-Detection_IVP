from flask import Flask,request,render_template

app = Flask(__name__)

@app.route('/')
def home():
    
    return render_template('index.html')

@app.route('/edge_detection',methods=['GET','POST'])
def edge():
    name = request.form['img']
    algo = request.form['algorithm']
    print(name)
    print(algo)

    return render_template('index.html')




if __name__ == "__main__":
    app.run(debug=True)