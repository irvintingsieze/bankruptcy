from flask import Flask
app = Flask(__name__)
from flask import request, render_template
from keras.models import load_model
@app.route("/",methods = ["GET","POST"])
def index():
    
    if request.method == "POST":
        NPTA = request.form.get("NPTA")
        TLTA = request.form.get("TLTA")
        WCTA = request.form.get("WCTA")
        print(NPTA,TLTA,WCTA)
        model = load_model("bankruptcy_model")
        pred = model.predict([[float(NPTA),float(TLTA),float(WCTA)]])
        return (render_template("index.html",result=pred))
    else:
        return (render_template("index.html",result="2"))
    
if __name__ == "__main__":
    app.run()