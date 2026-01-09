# step-1 : import your flask

from flask import Flask , request

# step-2 : Initilaise flask object here

app=Flask(__name__)

# step-3 : Create endpoint or route + Logic
@app.route('/name')
def uppercase_name():
    name = request.args.get('name')

    if not name:
        return ' Please provide name as a query parameter.'

    return f' {name.strip().upper()}'

# step4 : Run the application

if __name__== '__main__':
    app.run(debug=True)