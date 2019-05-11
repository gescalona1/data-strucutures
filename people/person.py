class Person:
    def __init__(self, *, first, last, type="Nano", email="@email"):
        self._first_name = first
        self._last_name = last
        self.type = type
        self.email = email

    @property
    def name(self):
        return f"{self._first_name} {self._last_name}"

