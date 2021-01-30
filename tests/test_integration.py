import unittest, importlib
from unittest.mock import patch
import itertools

circuits = importlib.import_module("01-introduction.circuits")

AndGate = getattr(circuits, "AndGate")
OrGate = getattr(circuits, "OrGate")
NandGate = getattr(circuits, "NandGate")
NorGate = getattr(circuits, "NorGate")
NotGate = getattr(circuits, "NotGate")
Connector = getattr(circuits, "Connector")


class TestIntegration(unittest.TestCase):
    def test_de_morgan(self):
        values = list(itertools.product((0, 1), repeat=4))
        de_morgan = lambda a, b, c, d: not ((a and b) or (c and d))
        for i in range(len(values)):
            with self.subTest(i=values[i]):
                with patch("builtins.input", side_effect=values[i]):
                    g1 = AndGate("G1")
                    g2 = AndGate("G2")
                    g3 = OrGate("G3")
                    g4 = NotGate("G4")
                    c1 = Connector(g1, g3)
                    c2 = Connector(g2, g3)
                    c3 = Connector(g3, g4)
                    self.assertEqual(g4.get_output(), de_morgan(*values[i]))
                with patch("builtins.input", side_effect=values[i]):
                    g1 = AndGate("G1")
                    g2 = AndGate("G2")
                    g3 = NorGate("G3")
                    c1 = Connector(g1, g3)
                    c2 = Connector(g2, g3)
                    self.assertEqual(g3.get_output(), de_morgan(*values[i]))
                with patch("builtins.input", side_effect=values[i]):
                    g1 = NandGate("G1")
                    g2 = NandGate("G2")
                    g3 = AndGate("G3")
                    c1 = Connector(g1, g3)
                    c2 = Connector(g2, g3)
                    self.assertEqual(g3.get_output(), de_morgan(*values[i]))
