import unittest, importlib
from unittest.mock import patch, MagicMock
from tests.test_logic_gate import TestLogicGate

circuits = importlib.import_module("01-introduction.circuits")

BinaryGate = getattr(circuits, "BinaryGate")


class TestBinaryGate(TestLogicGate):

    gate_class = BinaryGate

    @patch("01-introduction.circuits.Connector")
    def test_connect(self, mock_connector):
        self.logic_gate.connect(mock_connector)
        self.assertIs(self.logic_gate.pin_a, mock_connector)
        self.logic_gate.connect(mock_connector)
        self.assertIs(self.logic_gate.pin_b, mock_connector)
        with self.assertRaises(RuntimeError):
            self.logic_gate.connect(mock_connector)

    @patch("01-introduction.circuits.Connector")
    def test_get_pin_a(self, mock_connector):
        with patch("builtins.input", return_value="1"):
            self.assertEqual(self.logic_gate.get_pin_a(), 1)
        mock_connector.get_from_gate.return_value.get_output.return_value = 0
        self.logic_gate.pin_a = mock_connector
        self.assertEqual(self.logic_gate.get_pin_a(), 0)

    @patch("01-introduction.circuits.Connector")
    def test_get_pin_b(self, mock_connector):
        with patch("builtins.input", return_value="0"):
            self.assertEqual(self.logic_gate.get_pin_b(), 0)
        mock_connector.get_from_gate.return_value.get_output.return_value = 1
        self.logic_gate.pin_b = mock_connector
        self.assertEqual(self.logic_gate.get_pin_b(), 1)

    def gate_logic_helper(self, logic_function):
        options = [(0, 0), (0, 1), (1, 0), (1, 1)]
        qualname = "{}.{}".format(
            type(self.logic_gate).__module__, type(self.logic_gate).__name__
        )
        with patch("{}.get_pin_a".format(qualname)) as mock_get_pin_a:
            with patch("{}.get_pin_b".format(qualname)) as mock_get_pin_b:
                for i in range(4):
                    with self.subTest(i=i):
                        (a, b) = options[i]
                        mock_get_pin_a.return_value = a
                        mock_get_pin_b.return_value = b
                        self.assertEqual(
                            self.logic_gate.perform_gate_logic(),
                            logic_function(a, b),
                        )
