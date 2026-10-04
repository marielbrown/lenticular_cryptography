import json

import indexer
import encoder

import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(help='subcommand help', dest="subcommand")

    parser_keygen = subparsers.add_parser('keygen', help='generate a key used for simultaneous encoding')
    parser_keygen.add_argument('key_a_path', help='path to the first cypher file')
    parser_keygen.add_argument('key_b_path', help='path to the second cypher file')

    parser_encode = subparsers.add_parser('encode', help='encode two messages into one cyphertext file')
    parser_encode.add_argument('secret_a_path', help='path to the secret which uses the first cypher')
    parser_encode.add_argument('secret_b_path', help='path to the secret which uses the second cypher')
    parser_encode.add_argument('key_path', help='path to lentigular cryptography key file')

    parser_dencode = subparsers.add_parser('decode', help='decode a message')
    parser_dencode.add_argument('message_path', help='path to the message to decrypt')
    parser_dencode.add_argument('key_path', help='path the the decryption cypher')

    parser.add_argument("-o", "--out", help="output file path")

    return parser.parse_args()

def write_out(out_string, file_path):
      with open(file_path, "w", encoding="utf-8") as out:
           out.write(out_string)   

def main(args):
        out_path = args.out
        if args.subcommand == "keygen":
            if (out_path == None): out_path = "./key" 

            key = indexer.index_files(args.key_a_path, args.key_b_path)
            write_out(str(key), out_path)
            print("key generated at ", out_path)
            
        elif args.subcommand == "encode":
            if (out_path == None): out_path = "./encoded_message.txt"

            key = encoder.load_key(args.key_path)
            encoded_message = encoder.encode(args.secret_a_path, args.secret_b_path, key)
            write_out(str(encoded_message), out_path)
            print("message encoded at ", out_path)

        elif args.subcommand == "decode": 
            if (out_path == None): out_path = "./decoded_msg.txt"

            decoded_message = encoder.decode(args.message_path, args.key_path)
            write_out(decoded_message, out_path)
            print("message decoded at ", out_path)

if __name__ == "__main__":
    args = parse_args()
    main(args)