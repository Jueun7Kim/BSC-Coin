from flask import *

app = Flask(__name__, template_folder='templates')

flag = "2023GSM{_Th1S_S1t3'S_FE_w@S_m@D3_by_G@0n_}"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = request.json
        money = data.get('money', 0)
        print(money)
        print(data)
        
        if money >= 50000:
            return render_template_string(flag)
        else:
            return render_template_string("돈부터 벌어오세요")
            
    else:
        rt = render_template('index.html')
    return rt

@app.route('/alert')
def alert():
    return render_template('alert.html')
    


if __name__ == "__main__":
    app.run(use_reloader=True)