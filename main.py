from flask import Flask, render_template, url_for, request
import pandas as pd
from  sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.externals import joblib
app=Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():
    df=pd.read_excel("Copy of maindata.xlsx")
    df_data=df[["SYMPTOMS","CLASS"]]
    print(df_data)
    df_x=df_data['SYMPTOMS']
    print(df_x)
    df_y=df_data.CLASS
    print(df_y)
    corpus=df_x
    cv=CountVectorizer()
    X=cv.fit_transform(corpus)
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X,df_y,test_size=0.33, random_state=42)
    from sklearn.naive_bayes import MultinomialNB
    clf=MultinomialNB()
    clf.fit(X_train,y_train)
    clf.score(X_test,y_test)


    if request.method == 'POST':
	    comment = request.form['comment']
	    data = [comment]
        
	    vect = cv.transform(data).toarray()
        
	    my_prediction = clf.predict(vect)
    return render_template('result.html',prediction = my_prediction)
    
@app.route('/diarrhea.html/')
def diarrhea():
    return render_template('diarrhea.html')
    

@app.route('/cancer.html/')
def cancer():
    return render_template('cancer.html')

@app.route('/chikankuniaya.html/')
def chikankuniaya():
    return render_template('chikankuniaya.html')

@app.route('/constipation.html/')
def constipation():
    return render_template('constipation.html')

@app.route('/dengue fever.html/')
def dengue_fever():
    return render_template('dengue fever.html')

@app.route('/fatigue.html/')
def fatigue():
    return render_template('fatigue.html')

@app.route('/fever.html/')
def fever():
    return render_template('fever.html')

@app.route('/kidney stone.html/')
def kidney_stone():
    return render_template('kidney stone.html')

@app.route('/lukemia.html/')
def lukemia():
    return render_template('lukemia.html')

@app.route('/stroke.html/')
def stroke():
    return render_template('stroke.html')

@app.route('/tuberculosis.html/')
def tuberculosis():
    return render_template('tuberculosis.html')

@app.route('/urinary infection.html/')
def urinary_infection():
    return render_template('urinary infection.html')

@app.route('/weight loss.html/')
def weight_loss():
    return render_template('weight loss.html')




if __name__=='__main__':
    app.run(debug=True)