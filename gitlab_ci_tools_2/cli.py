"""Console script for gitlab_ci_tools_2."""
import argparse
import sys

from gitlab_ci_tools_2.b64_util import encode_decode


def main():
    """Console script for gitlab_ci_tools_2."""
    parser = argparse.ArgumentParser()
    parser.add_argument('action', choices=['encrypt', 'decrypt'])
    parser.add_argument('environment', choices=['staging', 'prod'])
    args = parser.parse_args()
    encode_decode(args)
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
