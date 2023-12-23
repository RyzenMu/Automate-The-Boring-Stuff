import smtplib
conn = smtplib.SMTP('smtp.gmail.com', 587)
print(type(conn))
print(conn.ehlo)
print(conn.ehlo_msg)

conn.starttls()

conn.login('muruga13in2022@gmail.com', 'nantham19')

conn.sendmail('muruga13in2022@gmail.com', 'muruga13in2022@gmail.com', 'Subject : so long...\n\n Dear Muruga, \n so long and thanks for \n\n - Muruga')
conn.quit() 