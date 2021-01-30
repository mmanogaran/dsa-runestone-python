import unittest, importlib
from unittest.mock import patch

circuits = importlib.import_module("01-introduction.circuits")

Connector = getattr(circuits, "Connector")
BinaryGate = getattr(circuits, "BinaryGate")
UnaryGate = getattr(circuits, "UnaryGate")


class TestConnector(unittest.TestCase):
    def test_binary_init(self):
        b1 = BinaryGate("b1")
        b2 = BinaryGate("b2")
        c1 = Connector(b1, b2)
        self.assertIs(c1.get_to_gate().pin_a, c1)
        c2 = Connector(b1, b2)
        self.assertIs(c2.get_to_gate().pin_b, c2)
        with self.assertRaises(RuntimeError):
            Connector(b1, b2)

    def test_unary_init(self):
        u1 = UnaryGate("u1")
        u2 = UnaryGate("u2")
        c = Connector(u1, u2)
        self.assertIs(c.get_to_gate().pin, c)
        with self.assertRaises(RuntimeError):
            Connector(u1, u2)

    def test_get_from_gate(self):
        from_gate = BinaryGate("b1")
        to_gate = BinaryGate("b2")
        c = Connector(from_gate, to_gate)
        self.assertIs(c.get_from_gate(), from_gate)

    def test_get_to_gate(self):
        from_gate = UnaryGate("u1")
        to_gate = UnaryGate("u2")
        c = Connector(from_gate, to_gate)
        self.assertIs(c.get_to_gate(), to_gate)