# Made by Luuk Klingens
# GitHub: https://github.com/devluuk123
# Copyright 2025
import base64


input = input("Enter a base64 encoded string to decode:")

decoded_bytes = base64.b64decode(str(input).encode("utf-8"))
decoded_str = str(decoded_bytes, "utf-8")


print("Decoded string:", decoded_str)