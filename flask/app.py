from flask import Flask, render_template, url_for, request, redirect, session
import requests
import json
import pyrebase
app=Flask(__name__)
config={
    'apiKey': "",
    'authDomain': "dcscproject-42b0a.firebaseapp.com",
    'projectId': "dcscproject-42b0a",
    'storageBucket': "dcscproject-42b0a.appspot.com",
    'messagingSenderId': "952120946916",
    'appId': "1:952120946916:web:cbce3696bba81ac7e6bcf1",
    'measurementId': "G-2LGRXCLHNQ",
    'databaseURL':""
}
firebase = pyrebase.initialize_app(config)
auth=firebase.auth()
app.secret_key='secret'
@app.route('/', methods=['POST','GET'])
def login():
    if('user' in session):
        return 'Hi ,{}'.format(session['user'])
    if request.method == 'POST':
        email=request.form.get('email')
        password=request.form.get('password')
        print(email,password)
        print("j")
        try:
            print("Hi")
            user = auth.sign_in_with_email_and_password(email,password)
            session['user'] = email
            return redirect('\home')
        except:
            print("b")
            return 'Failed to login'
    return render_template('login.html')
@app.route("/signup", methods=['POST','GET'])
def signup():
    if request.method == 'POST':
        
        try:
            
            print(request.form)
            email=request.form.get('email')
            password=request.form.get('password')
            print(email,password)
            new_user = auth.create_user_with_email_and_password(email,password)
            return redirect('/')


        # auth.create_user_with_email_and_password(email,password)   
        except:
            return 'Cant sign in'
    
    return render_template('signup.html')

@app.route('/home', methods=['POST','GET'])
def home():
    overpass_url = "http://overpass-api.de/api/interpreter"
    overpass_query = """
    [out:json];
    area["ISO3166-2"="US-CO"][admin_level=4];
    (node["amenity"="restaurant"](area);
    way["amenity"="restaurant"](area);
    rel["amenity"="restaurant"](area);
    );
    out center;
    """
    response = requests.get(overpass_url, params={'data': overpass_query})

    data = response.json()
    res = list()
    for dat in data['elements']:
        for key,value in dat['tags'].items():
            if (key == "addr:city"):
                res.append(value)
    lst = []
    [lst.append(x) for x in res if x not in lst]
    res1=[]
    lst1=[]
    for dat in data['elements']:
        for key,value in dat['tags'].items():
            if (key == "cuisine"):
                res1.append(value)
    
    [lst1.append(x) for x in res1 if x not in lst1]
    res2=[]
    lst2=[]
    for dat in data['elements']:
        for key,value in dat['tags'].items():
            if (key == "opening_hours"):
                res2.append(value)
    
    [lst2.append(x) for x in res2 if x not in lst2]
               
    return render_template('test.html', lst=lst, lst1=lst1, lst2=lst2)
    
@app.route('/submit-form', methods = ['GET', 'POST'])
def submitForm():
    overpass_url = "http://overpass-api.de/api/interpreter"
    overpass_query = """
    [out:json];
    area["ISO3166-2"="US-CO"][admin_level=4];
    (node["amenity"="restaurant"](area);
    way["amenity"="restaurant"](area);
    rel["amenity"="restaurant"](area);
    );
    out center;
    """
    response = requests.get(overpass_url, params={'data': overpass_query})

    data = response.json()
    if request.method == "POST":
        selectValue = request.form.get('lst')
        selectValue1 =request.form.get('lst1')
        selectValue2 = request.form.get('lst2')
        result={}
        for dat in data['elements']:
             for key,value in dat['tags'].items():
                if (key == "addr:city" and value==selectValue):
                    for k,v in dat['tags'].items():
                        if (k == "cuisine" and v==selectValue1):
                            result[dat['id']] = dat['tags']
        

                                    
        
        return render_template('try.html',selectValue=selectValue, selectValue1=selectValue1, selectValue2=selectValue2, result=result)
    return render_template("try.html", selectValue="Select a Value")

@app.route('/logout', methods=['GET','POST'])
def logout():
    x=session.pop('user')
    print(x)
    return redirect('/')
if __name__=='__main__':
    app.run(debug=True)
