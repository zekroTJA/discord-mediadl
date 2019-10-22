import args
import discord
import download


def main():
    argv = args.get_parsed_args()
    dc = discord.Discord(argv.token)
    dl = download.Download()

    res = dc.get_all_channel_messages(argv.channel)
    for msg in res:
        dl.download_image_from_message(msg)


if __name__ == '__main__':
    main()
