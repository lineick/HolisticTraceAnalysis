import json
import argparse
import random
import os

def process_trace(input_path, output_path, n, seed=None):
    with open(input_path, 'r') as f:
        data = json.load(f)

    if "traceEvents" not in data or not isinstance(data["traceEvents"], list):
        raise ValueError("Input JSON must contain a 'traceEvents' array.")

    events = data["traceEvents"]

    if seed is not None:
        random.seed(seed)
        data["traceEvents"] = random.sample(events, min(n, len(events)))
    else:
        data["traceEvents"] = events[:n]

    with open(output_path, 'w') as f:
        json.dump(data, f, indent=2)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Trim or sample the 'traceEvents' array in a PyTorch profiler trace.")
    parser.add_argument("input", help="Input JSON file")
    parser.add_argument("-n", type=int, required=True, help="Number of traceEvents to keep")
    parser.add_argument("--seed", type=int, help="Random seed for sampling")
    parser.add_argument("--output", help="Output JSON file (default: <input>_cut.json)")

    args = parser.parse_args()
    output = args.output or f"{os.path.splitext(args.input)[0]}_cut.json"
    process_trace(args.input, output, args.n, args.seed)
