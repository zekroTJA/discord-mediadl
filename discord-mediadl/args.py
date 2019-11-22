import argparse


def get_parsed_args():
    parser = argparse.ArgumentParser("discord message script")
    parser.add_argument('--token', required=True, type=str, help='Discord Bot Token')
    parser.add_argument('--channel', required=True, type=str, help='Channel\'s ID')
    parser.add_argument('--output', default='./out', type=str, help='Output Directory for Downloads')
    parser.add_argument('--analyze', default=False, type=bool, help='Whether or not to analyze statistics')
    return parser.parse_args()
