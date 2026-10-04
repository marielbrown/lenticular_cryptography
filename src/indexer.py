# get char streams of 2 files
# iterate over streams, adding each index to hash map of tuples
# save map? as private key


def index_files(path_a, path_b):
    charmap = {}

    with open(path_a, encoding="utf-8") as file_a:
        with open(path_b, encoding="utf-8") as file_b:

            index = 0
            char_a = file_a.read(1)
            char_b = file_b.read(1)

            # loop until EOF of either file
            while char_a != "" and char_b != "":
                entry = (char_a, char_b)
                key_list = charmap.get(entry, [])
                key_list.append(index)
                charmap[entry] = key_list;

                char_a = file_a.read(1)
                char_b = file_b.read(1)
                index += 1

    return charmap
