#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask, request, render_template
app = Flask(__name__) #this mean the website is under my name for legal use

@app.route("/", methods=["GET","POST"])
def index():
    if request.method == "POST":
        rate = float(request.form.get("rate"))
        print(rate)
        return(render_template("index.html", result= -50.6*rate + 90.2))
    
    else:
        return(render_template("index.html", result="waiting for exchange rate..."))

if __name__ == "__main__":  #double check it's under my name
    app.run()


# In[4]:


pip install flask


# In[ ]:




