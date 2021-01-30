from abc import ABC, abstractmethod


class LogicGate:
    def __init__(self, label):
        self.label = label
        self.output = None

    def get_label(self):
        return self.label

    def get_output(self):
        self.output = self.perform_gate_logic()
        return self.output

    @abstractmethod
    def perform_gate_logic(self):
        raise NotImplementedError

    @abstractmethod
    def connect(self, connector):
        raise NotImplementedError


class BinaryGate(LogicGate):
    def __init__(self, label):
        super().__init__(label)

        self.pin_a = None
        self.pin_b = None

    def get_pin_a(self):
        if self.pin_a == None:
            return int(
                input("Enter Pin A input for gate " + self.get_label() + "-->")
            )
        else:
            return self.pin_a.get_from_gate().get_output()

    def get_pin_b(self):
        if self.pin_b == None:
            return int(
                input("Enter Pin B input for gate " + self.get_label() + "-->")
            )
        else:
            return self.pin_b.get_from_gate().get_output()

    def connect(self, connector):

        if self.pin_a == None:
            self.pin_a = connector
        elif self.pin_b == None:
            self.pin_b = connector
        else:
            raise RuntimeError("Error: No empty pins for connector")


class UnaryGate(LogicGate):
    def __init__(self, label):
        super().__init__(label)

        self.pin = None

    def get_pin(self):
        if self.pin == None:
            return int(
                input("Enter Pin input for gate " + self.get_label() + "-->")
            )
        else:
            return self.pin.get_from_gate().get_output()

    def connect(self, connector):
        if self.pin == None:
            self.pin = connector
        else:
            raise RuntimeError("Error: No empty pins for connector")


class AndGate(BinaryGate):
    def __init__(self, label):
        super().__init__(label)

    def perform_gate_logic(self):
        a = self.get_pin_a()
        b = self.get_pin_b()

        return 1 if ((a == 1) and (b == 1)) else 0


class OrGate(BinaryGate):
    def __init__(self, label):
        super().__init__(label)

    def perform_gate_logic(self):
        a = self.get_pin_a()
        b = self.get_pin_b()

        return 1 if ((a == 1) or (b == 1)) else 0


class NotGate(UnaryGate):
    def __init__(self, label):
        super().__init__(label)

    def perform_gate_logic(self):
        pin = self.get_pin()

        return 1 if (pin == 0) else 0


class NandGate(AndGate):
    def __init__(self, label):
        super().__init__(label)

    def perform_gate_logic(self):
        return 1 if (super().perform_gate_logic() == 0) else 0


class NorGate(OrGate):
    def __init__(self, label):
        super().__init__(label)

    def perform_gate_logic(self):
        return 1 if (super().perform_gate_logic() == 0) else 0


class Connector:
    def __init__(self, from_gate, to_gate):
        self.from_gate = from_gate
        self.to_gate = to_gate

        to_gate.connect(self)

    def get_from_gate(self):
        return self.from_gate

    def get_to_gate(self):
        return self.to_gate


if __name__ == "__main__":
    g1 = AndGate("G1")
    g2 = AndGate("G2")
    g3 = OrGate("G3")
    g4 = NotGate("G4")
    c1 = Connector(g1, g3)
    c2 = Connector(g2, g3)
    c3 = Connector(g3, g4)
    print(g4.get_output())