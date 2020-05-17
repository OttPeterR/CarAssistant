"""This is the main method of the entire system"""

import sys
import argparse
import asyncio


def get_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Car Assisstant: Automate and monitor your car!"
    )
    parser.add_argument("--log_level", type=int, default=1, required=False)
    parser.add_argument("-v", "--verbose", action="store_true", required=False)
    parser.add_argument("--gps", action="store_true", required=False)

    arguments = parser.parse_args()
    return arguments


def run_car_assistant(args: argparse.Namespace) -> int:
    return 1


def main() -> int:
    """Start Car Assistant"""
    args = get_arguments()
    exit_code = asyncio.run(run_car_assistant(args))
    return exit_code


if __name__ == "__main__":
    sys.exit(main())
