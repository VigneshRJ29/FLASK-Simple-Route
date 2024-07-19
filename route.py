from flask import Flask
app=Flask("__name__")
@app.route('/')
def name():
    return "<div><center><h1>Hello</h1></center></div>"
@app.route('/next')
def next():
    return "<div><center><h1> World</h1></center></div>"
@app.route('/next/full')
def full():
    return "<div><center><h1> Hello World</h1></center></div>"
if __name__=="__main__":
    app.run(debug=True)