import flask
import joblib

app = flask.Flask(__name__)

@app.route("/predict",methods=["GET"])
def predict():
    loaded_model=joblib.load('/mnt/c/trained_model')

    if flask.request.method == "GET":
        if flask.request.args.get("exp"):
          try:
            exp=float(flask.request.args.get("exp"))
            predicted_value=loaded_model.predict([[exp]])
            return str(predicted_value[0])
          except Exception as e:
            print(e)
            return "Please provide a valid exp"
        else:
          return "Please provide a exp"
    else:
      return "Method Not Allowed"


if __name__ == '__main__':
   app.run(host='0.0.0.0',port=8080)