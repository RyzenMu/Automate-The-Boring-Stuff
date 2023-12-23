import imapclient
conn = imapclient.IMAPClient('imap.gmail.com', ssl=True)
conn.login('muruga13in2022@gmail.com', 'nantham@19')
conn.select_folder('INBOX', readonly=True) # readonly = False for deleting an email

print(conn.list_folders()) # prinst lists of folders
uids = conn.search(['SINCE 02-Aug-2022'])
raw_message = conn.fetch([uids[0]], ['BODY[]', 'FLAGS'])

# to delte a email
conn.delete_messages([uids[0]])

import pyzmail
message = pyzmail.PyzMessage.factory(raw_message[uids[0][b'BODY[]']])
print(message.get_subject())
print(message.get_address('from'))
print(message.get_address('to'))
print(message.get_address('cc'))
print(message.text_part == None)
print(message.html_part == None)
print(message.text_part.get_payload().decode('UTF-8'))