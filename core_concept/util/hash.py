from hashlib import sha256

def generate_hash(str):
  hash = sha256(str.encode("UTF-8"))
  digest = hash.hexdigest()
  return digest

def check_hash(str,hash_val):
  str_hash = generate_hash(str)
  if hash_val == str_hash:
    return True
  else:
    return False