import args
import discord
import download
import analyze


def main():
    argv = args.get_parsed_args()
    dc = discord.Discord(argv.token)

    res = dc.get_all_channel_messages(argv.channel)

    if argv.analyze:
        analyze.analyze(res)
        return

    dl = download.Download(argv.output)
    for msg in res:
        dl.download_image_from_message(msg)


if __name__ == '__main__':
    main()
