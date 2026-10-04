import json
import random

def load_key(key_path):
    with open(key_path, "r",  encoding="utf-8") as key_file:
        key_str = key_file.readline();
        #as_dict = json.loads(key_str)
        as_dict = eval(key_str)
        return as_dict

def encode(path_a, path_b, key_map):
    with open(path_a, encoding="utf-8") as file_a:
        with open(path_b, encoding="utf-8") as file_b:

            encrypted = []

            char_a = file_a.read(1)
            char_b = file_b.read(1)

            # loop until EOF of both files
            while char_a != "" or char_b != "":
                if char_a == "": char_a = " "
                if char_b == "": char_b = " "

                keys = key_map[(char_a, char_b)]
                selected : int = random.choice(keys)
                encrypted.append(selected)

                char_a = file_a.read(1)
                char_b = file_b.read(1)

    return encrypted

def decode(cypher_path, key_path):
    message = ""

    with open(key_path, encoding="utf-8") as key_file:
        with open(cypher_path, encoding="utf-8") as msg_file:

            key = key_file.read()
            cypher_text = eval(msg_file.read())
            for code in cypher_text:
                message += key[code]

    return message;
    