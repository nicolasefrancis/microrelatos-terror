from flask import Flask, render_template, request
from markov_model import sentence

app = Flask(__name__)

ESCENARIOS = ["bosque", "pueblo costero", "mansión", "cementerio"]
EPOCAS = ["1890", "actualidad", "futuro cercano", "post-apocalipsis"]
MONSTRUOS = ["fantasma", "demonio",
             "criatura lovecraftiana", "inteligencia maligna"]

TEMPLATE = (
    "En un {escenario} durante {epoca}, "
    "un {monstruo} acecha entre sombras. "
    "{cuerpo}"
)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        data = {
            "escenario": request.form["escenario"],
            "epoca":     request.form["epoca"],
            "monstruo":  request.form["monstruo"],
        }
        cuerpo = sentence()
        relato = TEMPLATE.format(**data, cuerpo=cuerpo)
        return render_template("result.html", relato=relato)
    return render_template(
        "index.html",
        escenarios=ESCENARIOS,
        epocas=EPOCAS,
        monstruos=MONSTRUOS,
    )


if __name__ == "__main__":
    app.run(debug=True)
