# Discord Media Download Script

This is a low level python script to download all attachments *(images, gifs, videos)* of a Discord channel. This script does not connect to Discords Gateway API, which makes this script verry leigh weight and does not require an implementation of an API wrapper like discord.py, for example.

---

## How to Use

First of all, clone the repository:
```
$ git clone git@github.com:zekroTJA/discord-mediadl.git \
    --branch master \
    --depth 1
```

After that, install required dependencies from `requirements.txt`:
```
$ python3 -m pip install -r requirements.txt
```

Folowing, you can make the script `dcdl` executable to use it as entry point for command execution:
```
$ chmod +x dcdl
```

Next, you can display the help text for further information how to use this script:
```
$ ./dcdl --help
```
*output:*
```
usage: discord message script [-h] --token TOKEN --channel CHANNEL
                              [--output OUTPUT] [--analyze ANALYZE]

optional arguments:
  -h, --help         show this help message and exit
  --token TOKEN      Discord Bot Token
  --channel CHANNEL  Channel's ID
  --output OUTPUT    Output Directory for Downloads
  --analyze ANALYZE  Whether or not to analyze statistics
```

To download all attachment media from a Discord channel, use following command:
```
$ ./dcdl \
    --token ${DISCORD_TOKEN} \
    --channel 2347823490123623 \
    --output ./output
```

Then, all images extracted will be saved to the specified output location with the `ID` of the attachment as file name.

---

© 2019 Ringo Hoffmann (zekro Development).
Covered by the MIT Licence.