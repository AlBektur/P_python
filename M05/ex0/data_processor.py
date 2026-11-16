#!/opt/pyenv/shims/python

from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    def __init__(self):
        self._queue = []
        self._rank = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self._queue:
            raise Exception("No data in queue")
        content = self._queue.pop(0)
        rank = self._rank
        self._rank += 1
        return (rank, content)


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            for i in data:
                if type(i) is not int and type(i) is not float:
                    return False
            return True
        if type(data) is int or type(data) is float:
            return True
        return False

    def ingest(self, data: Any) -> None:
        if self.validate(data):
            if type(data) is list:
                for x in data:
                    self._queue.append(x)
            else:
                self._queue.append(data)
        else:
            raise Exception("Improper numeric data")


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if type(data) is list:
            for i in data:
                if type(i) is not str:
                    return False
            return True
        if type(data) is str:
            return True
        return False

    def ingest(self, data: Any) -> None:
        if self.validate(data):
            if type(data) is list:
                for x in data:
                    self._queue.append(x)
            else:
                self._queue.append(data)
        else:
            raise Exception("Improper numeric data")


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if type(data) is list:
            for i in data:
                if type(i) is not dict:
                    return False
            return True
        if type(data) is dict:
            return True
        return False

    def ingest(self, data: Any) -> None:
        if self.validate(data):
            if type(data) is list:
                for x in data:
                    if type(x) is dict:
                        for k, v in x.items():
                            s = f"{k}: {v}"
                            self._queue.append(s)
                    # else:

                    #     self._queue.append(x)
            else:
                (k, v), = data.items()
                s = f"{k}: {v}"
                self._queue.append(s)
        else:
            raise Exception("Improper numeric data")


def test_np() -> None:
    try:
        np = NumericProcessor()
        print("Testing Numeric Processor...")
        print(f"Trying to validate input '42': {np.validate(42)}")
        print(f"Trying to validate input 'Hello': {np.validate('Hello')}")
        print(
            "Test invalid ingestion of string 'foo'without prior validation:")
        np.ingest('foo')
    except Exception as e:
        print(f"Got exception: {e}")

    print("Processing data: [1, 2, 3, 4, 5]")
    np.ingest([1, 2, 3, 4, 5])
    print("Extracting 3 values...")
    for i in range(3):
        rank, content = np.output()
        print(f"Numeric value {rank}: {content}")


def test_tp() -> None:
    print("\nTesting Text Processor...")

    tp = TextProcessor()
    print(f"Trying to validate input '42': {tp.validate(42)}")

    print("Processing data: ['Hello', 'Nexus', 'World']")
    data = ['Hello', 'Nexus', 'World']
    tp.ingest(data)

    print("Extracting 1 value...")
    rank, content = tp.output()
    print(f"Text value {rank}: {content}")


def test_lp() -> None:
    print("\nTesting Log Processor...")

    lp = LogProcessor()
    print(f"Trying to validate input 'Hello': {lp.validate('hello')}")
    data = [{'log_level': 'NOTICE', 'log_message': 'Connection to server'},
            {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}]

    lp.ingest(data)
    print("Extracting 2 values...")
    for i in range(2):
        rank, value = lp.output()
        print(f"Log entry: {rank}: {value}")


if __name__ == "__main__":
    print("=== Code Nexus - Data Processor ===\n")

    test_np()

    test_tp()

    test_lp()
