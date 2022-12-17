from flask import Flask, render_template
app = Flask(_name_)
@app.route(target="_blank">@app.route("/index")
def first_webpage():
    name = 'Flask'
    return render_template('index.html', index_variable = name)
    app.run(debug=True)