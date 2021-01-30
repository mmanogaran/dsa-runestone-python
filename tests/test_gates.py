import unittest, importlib
from unittest.mock import patch

from tests.test_binary_gate import TestBinaryGate
from tests.test_unary_gate import TestUnaryGate

circuits = importlib.import_module("01-introduction.circuits")

AndGate = getattr(circuits, "AndGate")
OrGate = getattr(circuits, "OrGate")
NandGate = getattr(circuits, "NandGate")
NorGate = getattr(circuits, "NorGate")
NotGate = getattr(circuits, "NotGate")


class TestAndGate(TestBinaryGate):

    gate_class = AndGate

    def test_perform_gate_logic(self):
        self.gate_logic_helper(lambda x, y: x and y)


class TestOrGate(TestBinaryGate):

    gate_class = OrGate

    def test_perform_gate_logic(self):
        self.gate_logic_helper(lambda x, y: x or y)


class TestNandGate(TestBinaryGate):

    gate_class = NandGate

    def test_perform_gate_logic(self):
        self.gate_logic_helper(lambda x, y: int(not (x and y)))


class TestNorGate(TestBinaryGate):

    gate_class = NorGate

    def test_perform_gate_logic(self):
        self.gate_logic_helper(lambda x, y: int(not (x or y)))


class TestNotGate(TestUnaryGate):

    gate_class = NotGate

    def test_perform_gate_logic(self):
        self.gate_logic_helper(lambda x: int(not (x)))


if __name__ == "__main__":
    unittest.main()