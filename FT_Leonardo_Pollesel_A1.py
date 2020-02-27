import numpy as np
import matplotlib.pyplot as plt
from flask import Flask
app = Flask(__name__)


@app.route("/periodsincos", methods=["GET", "POST"])
def sincos():
    x = np.arange(0, 2 * np.pi, 0.01)
    y = np.sin(x)
    z = np.cos(x)
    plt.plot(x, y, x, z)
    plt.title("One period of cos and sin")
    plt.legend(["sin(x)", "cos(x)"])
    plt.savefig("sincos.png")
    return f"""
    <html>
    <body>
        <img src="/home/ec2-user/test/sincos.png" align="center">
    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
