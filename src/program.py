import json

from slack_converter import list_folder, get_json
from datetime import datetime


def main():
    print("Convert Slack Daily Standup to Markdown human readable and compilable")
    path, filenames = list_folder("/home/hermansen/Documents/git/converge/daily-standup/raw")

    dates = []
    for filename in filenames:
        filepath = path + '/' + filename
        dates.append(get_json(filepath))

    contents = []
    for date in dates:
        for item in date:
            try:
                messages = []
                if item['type'] == 'message' and item['subtype'] == 'bot_message':
                    for message in item['attachments']:
                        messages.append({
                            'title': message['title'],
                            'text': message['text']
                        })
                    contents.append({
                        'user': item['username'],
                        'date': datetime.fromtimestamp(int(item['ts'].split('.')[0])).strftime("%Y-%m-%d, %H:%M:%S"),
                        'messages': messages
                    })
            except:
                continue

    # Write to markdown
    f = open('/home/hermansen/Documents/git/converge/daily-standup/out/all.md', 'w')
    f.write("# Converge Daily Standup\n")
    for item in contents:
        if item['user'] == 'converge.kjuulh' or item['user'] == 'Geekbot':
            f.write('- Name: ' + "Kasper Juul Hermansen")
        elif item['user'] == 'Samir Habibi':
            f.write('- Name: ' + "Samir Habibi")
        else:
            break
        f.write('\n')
        f.write('  - Date: ' + item['date'])
        f.write('\n')
        for message in item['messages']:
            f.write('  - Question: ' + message['title'])
            f.write('\n')
            f.write('  - Answer: ' + message['text'])
            f.write('\n')
    f.write('\n')

    f = open('/home/hermansen/Documents/git/converge/daily-standup/out/all.md', 'w')
    f.write("# Converge Daily Standup\n")
    for item in contents:
        if item['user'] == 'converge.kjuulh' or item['user'] == 'Geekbot':
            f.write('- Name: ' + "Kasper Juul Hermansen")
        elif item['user'] == 'Samir Habibi':
            f.write('- Name: ' + "Samir Habibi")
        else:
            break
        f.write('\n')
        f.write('  - Date: ' + item['date'])
        f.write('\n')
        for message in item['messages']:
            f.write('  - Question: ' + message['title'])
            f.write('\n')
            f.write('  - Answer: ' + message['text'])
            f.write('\n')
    f.write('\n')


if __name__ == '__main__':
    main()
