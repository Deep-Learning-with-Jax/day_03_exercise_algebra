"""Test the data loading."""

import numpy as np
import pandas


def test_loader():
    """See if the keys and shapes check out."""
    rhein = pandas.read_csv("./data/pegel.tab", sep=" 	")
    levels = np.array([int(pegel.split(" ")[0]) for pegel in rhein["Pegel"]])
    assert rhein.keys()[0] == "Zeit"
    assert rhein.keys()[1] == "Pegel"
    assert rhein["Pegel"].shape == (195086,)
    assert levels.shape == (195086,)
