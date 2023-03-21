from flask import Flask, request, render_template
app = Flask(__name__)
def imc(a,b):
    return a / (b**2)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/post')
def homePost():
    return render_template('homePost.html')

@app.route('/get')
def homeGet():
    return render_template('homeGet.html')



@app.route('/data', methods=['GET', 'POST'])
def data():
    if request.method == 'GET':
        nome = request.args.get('nome')
        altezza =float(request.args.get('altezza'))
        peso =float(request.args.get('peso'))
        IMC = imc(peso,altezza)
        sesso = request.args.get('sesso')
        hobbies = request.args.getlist('hobbies')
        citta = request.args.get('citta')
        presentazione = request.args.get('presentazione')
        x=""
        immagine=""
        if IMC>25:
            x="sovrappeso"
            immagine="../static/img/sovrappeso"
        elif IMC>24.9 and IMC<18.5:
            x="normopeso"
            immagine="../static/img/normopeso"
        elif IMC < 18.4:
             x="sottopeso"
            immagine="../static/img/sottopeso"
    else:
        nome = request.form['nome']
        altezza =  float(request.form['altezza'])
        peso =float(request.form['peso'])
        IMC = imc(peso,altezza)
        sesso = request.form['sesso']
        hobbies = request.form['hobbies']
        citta = request.form['citta']
        presentazione = request.form['presentazione']

    return render_template('riepilogo.html', nome=nome, altezza=altezza, peso=peso, IMC=IMC, sesso=sesso, hobbies=hobbies, citta=citta, presentazione=presentazione)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)