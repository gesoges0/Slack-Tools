from argparse import ArgumentParser
from os import pardir

from chat import notify, send, write_attachment, show_attachments, send_attachments

if __name__ == '__main__':
    parser = ArgumentParser(description='slack tool')
    subparsers = parser.add_subparsers(help='sub-commands')
    subparsers.required = True
    subparsers.dest = 'SUB_COMMAND'

    # 単純テキストを作成、送信
    parser_notify = subparsers.add_parser('notify', help='テキストメッセージを送信する')
    parser_notify.add_argument('TEXT', type=str, help='メッセージ')
    parser_notify.set_defaults(func=notify)

    # attachmentを作成、送信
    parser_send = subparsers.add_parser('send', help='payloadを送信する')
    parser_send.add_argument('TEXT', type=str, help='メッセージ')
    parser_send.add_argument('--color', '-c', default='good')
    parser_send.add_argument('--title', '-t', default='title')
    parser_send.add_argument('--text', default='no text')
    parser_send.set_defaults(func=send)

    # attachmentを作成
    parser_write = subparsers.add_parser('write_attachment', help='attachmentを保存')
    parser_write.add_argument('--no', '-n', default=0, help='attachment no')
    parser_write.add_argument('--color', '-c', default='good')
    parser_write.add_argument('--title', '-t', default='title')
    parser_write.add_argument('--text', default='no text')
    parser_write.add_argument('--image_url', default='')
    parser_write.set_defaults(func=write_attachment)

    # attachmentを表示
    parser_get = subparsers.add_parser('show_attachments', help='attachmentを取得')
    parser_get.add_argument('--no', '-n', default=-1, type=int, help='all: -1')
    parser_get.set_defaults(func=show_attachments)

    # attachmentsを送信
    parser_send = subparsers.add_parser('send_attachments', help='attachmentを送信')
    parser_send.add_argument('--no', '-n', default=0, type=int, help='送信するattachmentの数')
    parser_send.add_argument('--thread_ts', default='', type=str, help='thread_ts')
    parser_send.add_argument('--text', default='text', type=str, help='text')
    parser_send.add_argument('--icon_emoji', default=':dog:', type=str, help='アイコン絵文字')
    parser_send.set_defaults(func=send_attachments)

    args = parser.parse_args()
    args.func(args)
