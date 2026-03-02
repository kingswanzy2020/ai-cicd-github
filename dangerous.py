# SAFE SCRIPT

# import subprocess
# import shlex
# import os


# def run_command(user_input):
#     """Run a shell command safely."""
#     args = shlex.split(user_input)
#     subprocess.call(args, shell=False)


# API_KEY = os.environ.get("API_KEY")


# SCRIPT FOR DANGEROUS CODE

import subprocess


def run_command(user_input):
    """Run a shell command from user input."""
    subprocess.call(user_input, shell=True)


API_KEY = "sk-live-abc123def456
