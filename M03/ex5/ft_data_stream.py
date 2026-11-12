#!/opt/pyenv/shims/python

import typing
import random


def gen_event() -> typing.Any:

    players = ['Alice', 'Bob', 'Dylan', 'Charlie']
    actions = ['run', 'eat', 'sleep', 'grab', 'move', 'climb', 'swim', 'use']
    res: tuple = (random.choice(players), random.choice(actions))
    yield res


def consume_event(event: list) -> typing.Any:
    for i in event:
        got = random.choice(b_list)
        b_list.remove(got)
        yield got


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")

    for i in range(1000):
        events = gen_event()
        ev = next(events)
        p, a = ev
        print(f"Event {i}: Player {p} did action {a}")

    b_list = []
    for i in range(10):
        events = gen_event()
        ev = next(events)
        b_list.append(ev)

    print(f"Built list of 10 events: {b_list}")
    for i in range(len(b_list)):
        got = consume_event(b_list)
        temp = next(got)
        print(f"Got event from list: {temp}")
        print(f"Remains in list: {b_list}")
