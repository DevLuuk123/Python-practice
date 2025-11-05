# Made by Luuk Klingens
# GitHub: https://github.com/devluuk123
# Copyright 2025
import base64

input = input("Enter a sentace to encode: ")
encoded_bytes = base64.b64encode(str(input).encode("utf-8"))
encoded_str = str(encoded_bytes, "utf-8")


print("Encoded string:", encoded_str)