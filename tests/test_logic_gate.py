import unittest, importlib
from unittest.mock import patch

circuits = importlib.import_module("01-introduction.circuits")

LogicGate = getattr(circuits, "LogicGate")


class TestLogicGate(unittest.TestCase):

    gate_class = LogicGate

    def setUp(self):
        super(TestLogicGate, self).setUp()
        self.logic_gate = self.gate_class("label")

    def tearDown(self):
        super(TestLogicGate, self).tearDown()
        del self.logic_gate

    def test_label(self):
        self.assertEqual(self.logic_gate.get_label(), "label")

    def test_output(self):
        with patch(
            "{}.{}.perform_gate_logic".format(
                type(self.logic_gate).__module__,
                type(self.logic_gate).__name__,
            )
        ) as mock_perform_gate_logic:
            mock_perform_gate_logic.return_value = 0
            self.assertEqual(self.logic_gate.get_output(), 0)
            mock_perform_gate_logic.return_value = 1
            self.assertEqual(self.logic_gate.get_output(), 1)

    def test_perform_gate_logic(self):
        with self.assertRaises(NotImplementedError):
            self.logic_gate.perform_gate_logic()

    @patch("01-introduction.circuits.Connector")
    def test_connect(self, mock_connector):
        with self.assertRaises(NotImplementedError):
            self.logic_gate.connect(mock_connector)


if __name__ == "__main__":
    unittest.main()