# There are many ways to convert between different number bases, here's one method in Python:

def convert_base(num, to_base=10, from_base=10):
  if isinstance(num, str):
    n = int(num, from_base)
  else:
    n = int(num)
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n < to_base:
      return alphabet[n]
    else:
      return convert_base(n // to_base, to_base) + alphabet[n % to_base]


# You can use this function to convert between any bases by specifying the to_base and from_base arguments. The default base is 10 (decimal), but you can convert to binary (base 2), octal (base 8), or hexadecimal (base 16) by passing the appropriate value for to_base.
