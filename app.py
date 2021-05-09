from flask import Flask, render_template, request
import scipy.stats as st
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def hello_world():
    request_type = request.method
    if request_type == 'GET':
        return render_template('output.html', op='')
    else:
        S = float(request.form['S'].strip())
        n = float(request.form['n'].strip())
        u = float(request.form['u'].strip())
        X = float(request.form['X'].strip())
        alpha = float(request.form['alpha'].strip())
        if S > 0 and n >0:
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
            output = "<h3>Output:</h3> \
            <div class='card bg-secondary text-white'> \
            <div class='card-body'><p>Z-value = " + str(Z) + "<br></p><p>For 1 tailed test: <br>" + one_tail + \
            "</p> <br><br><p>For 2 tailed test: <br> " + two_tail + "</p>"
            return render_template('output.html', op=output)
        else:
            output = "<h3>Output:</h3> \
            <div class='card bg-secondary text-white'> \
            <div class='card-body'>Enter Valid Input"
            return render_template('output.html', op=output)

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