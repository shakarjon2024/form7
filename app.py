from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/form7', methods=['GET', 'POST'])
def form7():
    if request.method == 'POST':
        xabar = request.form.get('xabar')
        return f"<h2>Sizning xabaringiz qabul qilindi!</h2><pre>{xabar}</pre><br><a href='/'>Orqaga</a>"
    return render_template('form7.html')

if __name__ == '__main__':
    app.run(debug=True)
