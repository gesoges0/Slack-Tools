import slackweb
import json
from utils import Option


option = Option()
slack = slackweb.Slack(url=option.incoming_webhook_url)

def notify(args):
    slack.notify(text = args.TEXT)

def send(args):
    color = args.color
    title = args.title
    text = args.text
    main_text = args.TEXT
    attachments = [{'color': color, 'title': title, 'text': text}]
    payload = {'text': main_text, 'attachments': attachments}
    slack.send(payload)

def write_attachment(args):
    color = args.color
    title = args.title
    text = args.text
    image_url = args.image_url
    attachment_no = args.no
    attachment = {'color': color, 'title': title, 'text': text, 'image_url': image_url}
    with open(f'/home/gesogeso/デスクトップ/Slack-Tools/src/attachment_{attachment_no}.json', 'w') as f:
        json_attachment = json.dump(attachment, f)

def show_attachments(args):
    no = args.no
    attachments = get_attachments(4)
    if no != -1:
        print(attachments[no])
    else:
        for v in attachments:
            print(v)

def get_attachments(no):
    attachments = []
    for i in range(no+1):
        attachment_json_path = f'/home/gesogeso/デスクトップ/Slack-Tools/src/attachment_{i}.json'
        with open(attachment_json_path, 'r') as f:
            attachment_dict = json.load(f)
            attachments.append(attachment_dict)
    return attachments

def send_attachments(args):
    no = args.no
    thread_ts = args.thread_ts
    text = args.text
    icon_emoji = args.icon_emoji
    username = args.username
    attachments = get_attachments(no)
    payload = {'text': text, 'attachments': attachments, 'icon_emoji': icon_emoji, 'username': username}
    if thread_ts:
        payload['thread_ts'] = thread_ts
    slack.send(payload)
    



    


