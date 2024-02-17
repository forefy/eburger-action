import argparse
import os
import sys
import uuid


def expand_excludes(user_input: str) -> list:
    options = ["low", "medium", "high"]
    input_to_index = {option: index + 1 for index, option in enumerate(options)}
    return options[: input_to_index.get(user_input, len(options))]


def set_multiline_output(name, value):
    with open(os.environ["GITHUB_OUTPUT"], "a") as fh:
        delimiter = uuid.uuid1()
        print(f"{name}<<{delimiter}", file=fh)
        print(value, file=fh)
        print(delimiter, file=fh)


# Parse action inputs
action_parser = argparse.ArgumentParser(description="eburger-action")
action_parser.add_argument("path", help="Path of the folder or file to scan")
action_parser.add_argument("exclude", nargs="?", help="Exclude finding severities")
action_parser.add_argument(
    "automatic_selection",
    type=int,
    help="Automatic selection from multiple projects in the same repo",
)
action_parser.add_argument("output_type", help="Results output file type")
action_args = action_parser.parse_args()

start_prompt = f"Analyzing path: {action_args.path}"
sys.argv = [sys.argv[0]]  # Reset sys.argv for eburger

from eburger.main import main
from eburger.utils.cli_args import args

args.solidity_file_or_folder = action_args.path
args.output = f"eburger-output.{action_args.output_type}"
args.debug = True
args.relative_file_paths = True
args.auto_selection = action_args.automatic_selection

if action_args.exclude:
    args.no = expand_excludes(action_args.exclude)
    start_prompt += f" with a {action_args.exclude} filter."

# Run eburger main function
main()

# Set the modified SARIF file as output for subsequent steps
set_multiline_output("sarif", args.output)
