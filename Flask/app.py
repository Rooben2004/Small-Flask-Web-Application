from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    # Get the form data
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    # Pass the data to the result template
    return render_template('result.html', name=name, email=email, message=message)

if __name__ == '__main__':
    app.run(debug=True)
