## Lenticular Book Cryptography
A programming experiment based on Eric Sultanic's Lenticrypt.
Generates a single ciphertext file such that different plaintexts are generated depending on which key is used for decryption.

This script indexes two cyphers (books) with a high combined entropy to create a combined key. Simultaneously encrypting two plain texts with the generated key will produce a single cypher text, which can be decrypted back into different plain texts depdending on which of the books is used as a decryption cypher.

## Attributions
Based on Eric Sultanic's Lenticrypt, as discussed in [PoC || GTFO issue 0x04](https://www.sultanik.com/pocorgtfo/#0x04)
Sultanic's implementation of Lenticrypt can be found [here](https://github.com/ESultanik/lenticrypt)

## Usage

Generate a shared key from two different book cyphers
```
$ python main.py keygen key_a_path key_b_path
```

Encode two secret messages into a single cyphertext using the previously generated key
```
$ python src/main.py encode secret_a_path secret_b_path key_path
```

Decode an encrypted message using a book cypher
```
$ python main.py decode [-h] message_path key_path
```