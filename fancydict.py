from typing import Any, Dict


class FancyDict(dict):
    def __init__(self, *args, **kwargs):
        super(FancyDict, self).__init__(*args, **kwargs)
        self.__dict__ = self


if __name__ == "__main__":
    test = {"a": "A", "b": "B", "c": "C"}
    ttest = FancyDict(test)
    print(ttest.a)