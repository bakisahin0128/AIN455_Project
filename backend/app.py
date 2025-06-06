from flask import Flask, render_template

app = Flask(__name__)

# Ana sayfayı gösteren rota
@app.route('/')
def ana_sayfa():
    return render_template('index.html')

# --- YENİ ---
# Robot seçildiğinde video sayfasını gösteren rota
@app.route('/robot')
def robot_sahnesi():
    return render_template('robot.html')

if __name__ == '__main__':
    app.run(debug=True)