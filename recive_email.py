import email
import imaplib

mail = imaplib.IMAP4_SSL('imap.mail.ru')
mail.login('forautotests@mail.ru', 'ghv9wuS3brnBusTBN4gn')

print(mail.list())
print(mail.select("elpts"))

result, data = mail.search(None, "ALL")
print(data)

ids = data[0]
print(ids)
id_list = ids.split()
print(id_list)
latest_email_id = id_list[-1]
print(latest_email_id)

result, data = mail.fetch(latest_email_id, "(RFC822)")
print(data)
raw_email = data[0][1]
print(raw_email)
raw_email_string = raw_email.decode('utf-8')
#print(raw_email_string)

email_message = email.message_from_string(raw_email_string)
print(email_message)
body = email_message.get_payload(decode=True).decode('utf-8')
print(body)
