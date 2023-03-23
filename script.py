from flask import Flask  
  
app = Flask(__name__) #creating the Flask class object   
 
@app.route('/home/<name>') #decorator drfines the   
def home(name):  
    return "hello"+name;  
  
if __name__ =='__main__':  
    app.run(debug = True)  