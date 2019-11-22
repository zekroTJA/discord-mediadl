
def get_attachment_count(msg):
    if msg is None:
        return 0

    attachments = msg.get('attachments')
    embeds = msg.get('embeds')

    c = 0

    if attachments is not None:
        c += len(attachments)

    if embeds is not None:
        c += len(embeds)
        
    return c


def analyze(msgs):
    msgs_map = {}
    user_map = {}

    for m in msgs:
        attachment_c = get_attachment_count(m)
        if attachment_c <= 0:
            continue

        author = m.get('author')
        if author is None:
            continue

        author_id = author.get('id')
        if author_id not in user_map:
            user_map[author_id] = author

        if author_id not in msgs_map:
            msgs_map[author_id] = attachment_c
        else:
            msgs_map[author_id] += attachment_c
            
    with open('analysis.csv', 'w', encoding='utf-8') as f:
        for k, v in msgs_map.items():
            a = user_map.get(k)
            if a is not None:
                line = ','.join([a.get('id'), a.get('username'), a.get('discriminator'), str(v)])
                print(line)
                f.write(line + '\n')
