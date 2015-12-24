from flask import Flask
from flask import request
from flask import render_template
from flask import request, redirect
from rcbl import recommend
import re
from Numb import numb
app = Flask(__name__)
@app.route('/go')
def my_form():
    return render_template("my-form.html")

@app.route('/go', methods=['POST'])
def recommendgo():
    humanity = request.form['five']
    sensitivity = request.form['sensitivity']
    text1 = request.form['text1']
    text2 = request.form['text2']
    text3 = request.form['text3']
    text4 = request.form['text4']
    text5 = request.form['text5']
    text6 = request.form['text6']
    text7 = request.form['text7']
    text8 = request.form['text8']
    text9 = request.form['text9']
    text10 = request.form['text10']
    text11 = request.form['text11']
    text12 = request.form['text12']
    text13 = request.form['text13']
    text14 = request.form['text14']
    text15 = request.form['text15']
    text16 = request.form['text16']
    text17 = request.form['text17']
    text18 = request.form['text18']
    text19 = request.form['text19']
    text20 = request.form['text20']
    text21 = request.form['text21']
    text22 = request.form['text22']
    text23 = request.form['text23']
    text24 = request.form['text24']
    text25 = request.form['text25']
    text26 = request.form['text26']
    text27 = request.form['text27']
    text28 = request.form['text28']
    text29 = request.form['text29']
    text30 = request.form['text30']
    
    arrkl = (int(humanity))
    
    a1='-empty-'
    a2='-empty-'
    a3='-empty-'
    a4='-empty-'
    a5='-empty-'
    a6='-empty-'
    a7='-empty-'
    a8='-empty-'
    a9='-empty-'
    a10='-empty-'
    a11='-empty-'
    a12='-empty-'
    a13='-empty-'
    a14='-empty-'
    a15='-empty-'
    
    
    if (arrkl>=2):
        a1 = str(str(numb(str(text1))[0])+":"+str(text16)+", ")
        
    if (arrkl>=2):
        a2 = str(str(numb(str(text2))[0])+":"+str(text17)+", ")

    if (arrkl>=2):
        a3 = str(str(numb(str(text3))[0])+":"+str(text18)+", ")

    if (arrkl>=2):
        a4 = str(str(numb(str(text4))[0])+":"+str(text19)+", ")

    if (arrkl>=2):
        a5 = str(str(numb(str(text5))[0])+":"+str(text20)+", ")

    if (arrkl>=2):
        a6 = str(str(numb(str(text6))[0])+":"+str(text21)+", ")

    if (arrkl>=2):
        a7 = str(str(numb(str(text7))[0])+":"+str(text22)+", ")

    if (arrkl>=2):
        a8 = str(str(numb(str(text8))[0])+":"+str(text23)+", ")

    if (arrkl>=2):
        a9 = str(str(numb(str(text9))[0])+":"+str(text24)+", ")

    if (arrkl>=2):
        a10 = str(str(numb(str(text10))[0])+":"+str(text25)+", ")

    if (arrkl>=2):
        a11 = str(str(numb(str(text11))[0])+":"+str(text26)+", ")

    if (arrkl>=2):
        a12 = str(str(numb(str(text12))[0])+":"+str(text27)+", ")

    if (arrkl>=2):
        a13 = str(str(numb(str(text13))[0])+":"+str(text28)+", ")

    if (arrkl>=2):
        a14 = str(str(numb(str(text14))[0])+":"+str(text29)+", ")

    if (arrkl>=2):
        a15 = str(str(numb(str(text15))[0])+":"+str(text30)+", ")
        
    
    rawent = re.sub(", +}","}",str("{"+a1+a2+a3+a4+a5+a6+a7+a8+a9+a10+a11+a12+a13+a14+a15+"}").replace("~~~:,",""))
    
    pm = "bvv"
    pv = str(rawent)
    #pv = "{1200:4.3,79132:5,608:4,296:5,318:5,1196:5,260:5,3578:5,56782:5,58559:4,72308:5,1089:5,6874:5,1214:4.7,1213:4.2,1221:3,70286:4.5,1198:3,1690:0.5,858:4.9,99114:4,135887:1,2710:4.1,1968:5}"
    #pv = "{79132:4,}"
    #attt = "bvv"
    #atttt = "{1200:4.3,79132:5,608:4,296:5,318:5,1196:5,260:5,3578:5,56782:5,58559:4,72308:5,1089:5,6874:5,1214:4.7,1213:4.2,1221:3,70286:4.5,1198:3,1690:0.5,858:4.9,99114:4,135887:1,2710:4.1,1968:5}"
    llll = recommend(pm,pv,minratingv=3,userstosourcev=14,minavgratingv=7,excludablev=True)#recommend(username,dtvv,minratingv=5,userstosourcev=30,minavgratingv=3,excludablev=True):
    return render_template(
            'nav.html',
            recs = llll[0],
            ratings = llll[1],
            )
            

if __name__ == '__main__':
    app.debug = True
    app.run()