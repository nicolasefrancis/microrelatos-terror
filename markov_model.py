import pathlib
import markovify

CORPUS_PATH = pathlib.Path("data/corpus.txt")
MODEL_JSON = pathlib.Path("data/model.json")


def build_model(state_size: int = 2):
    """Construye un modelo Markov a partir del corpus de texto."""
    text = CORPUS_PATH.read_text(encoding="utf8")
    return markovify.Text(text, state_size=state_size)


def load_model():
    """Carga el modelo desde disco o lo genera si no existe."""
    if MODEL_JSON.exists():
        return markovify.Text.from_json(MODEL_JSON.read_text())
    model = build_model()
    MODEL_JSON.write_text(model.to_json())
    return model


MODEL = load_model()


def sentence(max_chars: int = 280) -> str:
    """Devuelve una oración generada que no supere max_chars."""
    return MODEL.make_sentence(max_chars=max_chars, tries=100)
