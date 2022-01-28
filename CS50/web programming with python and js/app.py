#  install flask using pip install flask
# start flask by imorting flask as shown below


from app import Flask
app=Flask(__name__)

# create a route by using @ and bracket at the end
@app.route('/')
def index():
    return "hello world"

@app.route('/david')
def david():
    return "hello david"
# alternatively
@app.route('/<string:name>')
def hello(name):
    name=name.capitalized()
    print(name)
    return "hello, {name}!"
app.run(debug=True)