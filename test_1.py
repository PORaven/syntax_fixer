class Test(Exception):
    def __init__(
        self, *args: object, description: str = "Hello, test pre-commit"
    ) -> None:
        super().__init__(*args)
        self.description = description

    def __repr__(self) -> str:
        return f"{self.description}"

    def add_object_property(self, option: dict[str | int, str | int]) -> None:
        self.properties = option
        return self

    def convert_abs(num: int) -> int:
        return abs(num)
