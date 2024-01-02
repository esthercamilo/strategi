import hashlib
import datetime


d = datetime.datetime(year=1970, month=1, day=1)

# Suas três strings
ts = str(int(datetime.datetime.now().timestamp()))
private = "91cab695f4d1c01bdac2e31eee4a40a0a63098ff"
public = "c222541c087bdf9263e3b006f8dfff62"

# Concatenando as strings
concatenated_string = ts + private + public

# Calculando o hash MD5 da string concatenada
hash_md5 = hashlib.md5(concatenated_string.encode()).hexdigest()

url = f"http://gateway.marvel.com/v1/public/characters?ts={ts}&apikey={public}&hash={hash_md5}&limit=2000"
print(url)

