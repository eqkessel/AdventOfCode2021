# ADVENT OF CODE 2021
# Challenge #01, part 1
# Ethan Kessel

def main(input: str):
    depths = list(map(int, input.split()))
    increasing = 0
    for idx in range(1, len(depths)):
        if depths[idx] > depths[idx - 1]:
            increasing += 1
    return increasing

from os import path
import time
if __name__ == "__main__":
    print("Advent of Code 2021")
    print("Challenge #01, part 1")
    print("Ethan Kessel")
    print("-" * 24)

    pwd = path.dirname(__file__)
    with open(path.join(pwd, "input.txt")) as input_file:
        print(f"Executing on input file\n{input_file.name}")
        print("-" * 24)

        start_time__ns = time.perf_counter_ns()
        result = main(input_file.read())
        end_time__ns = time.perf_counter_ns()
        exec_time__us = (end_time__ns - start_time__ns) / 1000.0

    print(f"\nExecution time: {exec_time__us:.1f}us\n\n{result=}\n")