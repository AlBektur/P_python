#!/opt/pyenv/shims/python
from abc import ABC, abstractmethod
from typing import Any, Protocol


class CsvPlugin():
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("CSV Output:")
        print(",".join(item for _, item in data))


class JsonPlugin():
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("JSON Output:")
        pairs = ", ".join(f'"item_{rank}": "{value}"' for rank, value in data)
        print("{" + pairs + "}")


class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        pass


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
                    self._queue.append(str(x))
            else:
                self._queue.append(str(data))
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
        def is_log_entry(entry: Any) -> bool:
            return (
                type(entry) is dict
                and "log_level" in entry
                and "log_message" in entry
            )

        if type(data) is list:
            return all(is_log_entry(entry) for entry in data)

        return is_log_entry(data)

    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")

        entries = data if type(data) is list else [data]

        for entry in entries:
            message = f"{entry['log_level']}: {entry['log_message']}"
            self._queue.append(message)


class DataStream(ABC):
    def __init__(self) -> None:
        self.process_list: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self.process_list.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for data in stream:
            flag = False
            for process in self.process_list:
                if process.validate(data) is True:
                    process.ingest(data)
                    flag = True
                    break
            if flag is False:
                print(
                    f"DataStream error - "
                    f"Can't process element in stream: {data}"
                    )

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")

        if not self.process_list:
            print("No processor found, no data")
        else:
            for process in self.process_list:
                name = process.__class__.__name__
                label = name.replace("Processor", " Processor")
                print(
                    f"{label}:  total {process._rank + len(process._queue)}"
                    f" items processed,"
                    f" remaining {len(process._queue)} on processor")

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for process in self.process_list:
            size = min(nb, len(process._queue))
            data = []
            for i in range(size):
                data.append(process.output())
            if data:
                plugin.process_output(data)


if __name__ == "__main__":
    print("=== Code Nexus - Data Pipeline ===\n")
    print("Initialize Data Stream...")
    stream = DataStream()
    stream.print_processors_stats()
    data_0 = [
        'Hello world', [3.14, -1, 2.71],
        [{
            'log_level': 'WARNING',
            'log_message': 'Telnet access! Use ssh instead'
        }, {
            'log_level': 'INFO',
            'log_message': 'User wil isconnected'
        }],
        42, ['Hi', 'five']]

    data_1 = [
        21, ['I love AI', 'LLMs are wonderful', 'Stay healthy'],
        [{
            'log_level': 'ERROR',
            'log_message': '500 server crash'
        }, {
            'log_level': 'NOTICE',
            'log_message': 'Certificate expires in 10 days'
        }],
        [32, 42, 64, 84, 128, 168], 'World hello']

    print("\nRegistering Processors")
    stream = DataStream()

    np = NumericProcessor()
    tp = TextProcessor()
    lp = LogProcessor()

    stream.register_processor(np)
    stream.register_processor(tp)
    stream.register_processor(lp)

    print(f"Send first batch of data on stream: {data_0}\n")
    stream.process_stream(data_0)

    stream.print_processors_stats()

    print("\nSend 3 processed data from each processor to a CSV plugin")
    csv = CsvPlugin()

    stream.output_pipeline(3, csv)
    print()
    stream.print_processors_stats()

    print(f"\nSend another batch of data: {data_1}")
    stream.process_stream(data_1)
    print()
    stream.print_processors_stats()
    print()
    print("\nSend 5 processed data from each processor to a JSON plugin:")
    json = JsonPlugin()

    stream.output_pipeline(5, json)
    print()
    stream.print_processors_stats()
