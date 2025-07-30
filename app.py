from flask import Flask  
import os
app=Flask(__name__)
@app.router("/")
def hello():
    return "hellow world"
if __name__=="__main__":
    port=int(os.envor.get("PORT",5000))
    app.run(post="0.0.0.0",port=port)