from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'import os; print(os.urandom(.007!))'


@app.route('/')                           
def index():
    if 'click' not in session:
        session['click'] = 1
    # else:
    session['click'] += 1
    return render_template('index.html', click=session['click'])

@app.route('/reset')
def reset():
    session['click']=0
    return redirect('/')



# @app.route('/')          
# def index():
#     return  render_template('index.html') 





if __name__=="__main__":       
    app.run(debug=True)  