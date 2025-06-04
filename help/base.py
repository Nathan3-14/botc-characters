from typing import Any, List


class Command:
    def __init__(self, name: str, aliases: List[str]) -> None:
        self.name = name
        self.aliases = aliases
    
    def __call__(self) -> Any:
        pass

    