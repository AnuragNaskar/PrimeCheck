from flask import Flask, render_template, request

app = Flask(__name__)

def is_prime(n):
    for i in range(2, int(n) - 1):
        if n % i == 0:
            return False
    return True

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    number = None
    if request.method == "POST":
        try:
            number = int(request.form["number"])
            if(is_prime(number)):
                result = f"{number} is a prime number."
            elif(not is_prime(number)):
                result = f"{number} is not a prime number."
        except ValueError:
            result = "Invalid input. Please enter an integer."
    return render_template("index.html", result=result, number=number)

if __name__ == "__main__":
    app.run(debug=True)
