from werkzeug.security import generate_password_hash, check_password_hash

password = 'dustin1234'
pass_hash = generate_password_hash(password)
# imprimir por consola
print(pass_hash)

# checkear que esté bien hasheado
print(check_password_hash(password=password, pwhash=pass_hash))