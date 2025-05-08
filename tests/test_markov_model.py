"""Tests básicos para markov_model.py"""

import sys, pathlib
sys.path.append(str(pathlib.Path(__file__).resolve().parents[1]))


from markov_model import sentence

def test_sentence_is_string() -> None:
    txt = sentence()
    assert isinstance(txt, str)

def test_sentence_length_max() -> None:
    txt = sentence(max_chars=140)
    assert len(txt) <= 140
