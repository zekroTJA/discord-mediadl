import argparse


def get_parsed_args():
    parser = argparse.ArgumentParser("discord message script")
    parser.add_argument('--token', required=True, type=str, help='Discord Bot Token')
    parser.add_argument('--channel', required=True, type=str, help="Channel's ID")
    return parser.parse_args()
