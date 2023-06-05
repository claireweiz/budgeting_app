from cryptography.fernet import Fernet


def encrypt(pwd, type):
    if type == 'pwd':
        with open('key.bin', 'rb') as key_file:
            key_read = key_file.read()
            f = Fernet(key_read)
            encrypted = f.encrypt(pwd.encode())
            key_file.close()
            with open('password.bin', 'ab') as pwd_list:
                pwd_list.write(encrypted+'\n'.encode())
                pwd_list.close()
    elif type == 'usr':
        with open('key.bin', 'rb') as key_file:
            key_read = key_file.read()
            f = Fernet(key_read)
            encrypted = f.encrypt(pwd.encode())
            key_file.close()
            with open('username.bin', 'rb') as usr_list:
                usrs = usr_list.readlines()
                for line in usrs:
                    decrypted = f.decrypt(line)
                    if pwd.encode() in decrypted:
                        print('This username is already in use.')
                        return False
            with open('username.bin', 'ab') as usr_list:
                usr_list.write(encrypted+'\n'.encode())
                usr_list.close()
                return True
    else:
        raise TypeError
        return False
        
usr_line = 0
def decrypt(pwd, type):
    global usr_line
    if type == 'pwd':
        with open('key.bin', 'rb') as key_file:
            key_read = key_file.read()
            f = Fernet(key_read)
            with open('password.bin', 'rb') as pwd_list:
                pwds = pwd_list.readlines()
                for i, line in enumerate(pwds):
                    if i == usr_line:
                        if pwd.encode() in f.decrypt(line):
                            return True
            return False
    elif type == 'usr':
        with open('key.bin', 'rb') as key_file:
            key_read = key_file.read()
            f = Fernet(key_read)
            with open('username.bin', 'rb') as usr_list:
                usrs = usr_list.readlines()
                for i, line in enumerate(usrs):
                    usr_line = i
                    if pwd.encode() in f.decrypt(line):
                        return True
        
            return False
    else:
        raise TypeError
        return False