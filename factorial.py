from flask import Flask

app = Flask(__name__)

def factorial(n):
    n = int(n)
    if n < 0:
        return "No se puede calcular el factorial de un número negativo"
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, abs(n) + 1):
            result *= i
        if n < 0:
            return -result
        else:
            return result

@app.route('/factorial/<num>', methods=['GET'])
def get_factorial(num):
    return str(factorial(num))

@app.route('/')
def get_main():
    return str("Dirígete a /factorial y coloca /(numero a calcular)")

if __name__ == '__main__':
    app.run(debug = True)