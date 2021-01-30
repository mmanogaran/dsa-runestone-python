import unittest, importlib
from unittest.mock import patch, MagicMock
from tests.test_logic_gate import TestLogicGate

circuits = importlib.import_module("01-introduction.circuits")

UnaryGate = getattr(circuits, "UnaryGate")


class TestUnaryGate(TestLogicGate):

    gate_class = UnaryGate

    @patch("01-introduction.circuits.Connector")
    def test_connect(self, mock_connector):
        self.logic_gate.connect(mock_connector)
        self.assertIs(self.logic_gate.pin, mock_connector)
        with self.assertRaises(RuntimeError):
            self.logic_gate.connect(mock_connector)

    @patch("01-introduction.circuits.Connector")
    def test_get_pin(self, mock_connector):
        with patch("builtins.input", return_value="1"):
            self.assertEqual(self.logic_gate.get_pin(), 1)
        mock_connector.get_from_gate.return_value = MagicMock()
        mock_connector.get_from_gate().get_output.return_value = 0
        self.logic_gate.pin = mock_connector
        self.assertEqual(self.logic_gate.get_pin(), 0)

    def gate_logic_helper(self, logic_function):
        options = [0, 1]
        qualname = "{}.{}".format(
            type(self.logic_gate).__module__, type(self.logic_gate).__name__
        )
        print()
        with patch("{}.get_pin".format(qualname)) as mock_get_pin:
            for i in range(2):
                with self.subTest(i=i):
                    value = options[i]
                    mock_get_pin.return_value = value
                    self.assertEqual(
                        self.logic_gate.perform_gate_logic(),
                        logic_function(value),
                    )
