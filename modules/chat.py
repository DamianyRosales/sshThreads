

host = input('ip>')
if not host == '1':
    username = input('host>') + "\n"
    password = input('password>') + "\n"

    credentials = open("credentials.txt", "w+")
    credentials.write(host + "\n")
    credentials.write(username)
    credentials.write(password)

    credentials.close()

