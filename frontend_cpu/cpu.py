from flask import Flask, render_template
app = Flask(__name__)

app.add_url_rule('/static/<path:filename>', endpoint='static', view_func=app.send_static_file)
@app.route('/')
def hello_world():
    return render_template('index.html')


    if __name__ == '__main__':
    	app.run(debug=True)