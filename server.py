from flask import Flask,request,render_template, url_for
import util
app = Flask(__name__)

@app.route('/')
def home():
    
    return render_template('index.html')

@app.route('/edge_detection',methods=['GET','POST'])
def edge():
    path = "./input_images/"
    name = str(request.form['img'])
    algo = request.form['algorithm']
    print(name)
    print(algo)
    img_path = path + name
    if(algo == 'sobel_x'):
        util.sobel_x(img_path)
    elif(algo == 'sobel_y'):
        util.sobel_y(img_path)
    elif(algo == 'sobel_xy'):
        util.sobel_xy(img_path)
    elif(algo == 'laplacian'):
        util.laplacian(img_path)
    elif(algo == 'canny'):
        util.canny(img_path)

    return render_template('index.html')




if __name__ == "__main__":
    app.run(debug=True)