import argparse


def get_parsed_args():
    parser = argparse.ArgumentParser("discord message script")
    parser.add_argument('--token', '-t', required=True, type=str, help='Discord Bot Token')
    parser.add_argument('--channel', '-c', required=True, type=str, help='Channel\'s ID')
    parser.add_argument('--output', '-o', default='./out', type=str, help='Output Directory for Downloads')
    parser.add_argument('--analyze', '-a', default=False, action='store_true', help='Whether or not to analyze statistics')
    return parser.parse_args()
