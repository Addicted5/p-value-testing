from flask import Flask, render_template, request
import scipy.stats as st
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def hello_world():
    request_type = request.method
    if request_type == 'GET':
        return render_template('base.html')
    else:
        S = float(request.form['S'].strip())
        n = float(request.form['n'].strip())
        u = float(request.form['u'].strip())
        X = float(request.form['X'].strip())
        alpha = float(request.form['alpha'].strip())
        Z, p = ztest(X,u,S,n)
        ptwo = p*2
        if p>alpha:
            two_tail = 'Fail to Reject null Hypothesis'
            one_tail = 'Fail to Reject null Hypothesis'
        else:
            if ptwo>alpha:
                two_tail = 'Fail to Reject null Hypothesis'
            else:
                two_tail = 'Null Hypothesis can be rejected'
            one_tail = 'Null Hypothesis can be rejected'
        return render_template('output.html', z_value=Z,text_one=one_tail,text_two=two_tail)

def ztest(X,u,S,n):
    Z = (X-u)/(S/(n**0.5))
    if Z<0:
        p = st.norm.cdf(Z)
    else:
        p = 1-st.norm.cdf(Z)
    p2 = p*2
    return Z, p
if __name__ == "__main__":
    app.run(port = 5001 , debug= False)