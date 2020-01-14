from flask import Flask, render_template
app = Flask(__name__,
            static_url_path='/static')

@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/contactus.html')
def contact():
    return render_template('contactus.html')

@app.route('/aboutus.html')
def about():
    return render_template('aboutus.html')

if __name__ == "__main__":
    app.run(debug=True)