#!/usr/bin/env python3

import args
import discord
import download
import analyze
from os import environ


def main():
    argv = args.get_parsed_args()
    token = environ.get("DISCORD_API_TOKEN", argv.token)

    dc = discord.Discord(token)

    res = dc.get_all_channel_messages(argv.channel)

    if argv.analyze:
        plot_size = tuple([int(n) for n in argv.plot_size.split(',')])
        analyze.analyze(res, argv.plot, plot_size)
        return

    dl = download.Download(argv.output)
    for msg in res:
        dl.download_image_from_message(msg)


if __name__ == '__main__':
    main()
