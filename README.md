# LZW
LZW (Lempel–Ziv–Welch) is a universal lossless data compression technique. This compression algorithm was developed by Abraham Lempel, Jakob Ziv, and Terry Welch. In hardware implementations, the algorithm is simple and has the potential for very high throughput. It is the algorithm used in the GIF image format and is part of the widely used Unix file compression utility compress.


## LZW Compression
LZW compression works by building a dictionary of sequences from the input data as it processes the stream. Initially, it starts with single characters and gradually adds longer sequences as they are encountered. These sequences are then replaced by shorter code values in the compressed output. The more frequently a sequence is repeated in the input data, the more efficiently it can be represented by its corresponding code. As a result, LZW becomes increasingly effective when compressing data with longer, repetitive patterns, reducing file size by substituting patterns with compact codes.

## LZW Decompression
LZW decompression works by reversing the process of compression. It starts with a dictionary of initial codes (usually representing single characters, such as ASCII values 0-255). As the compressed data is processed, the dictionary is rebuilt dynamically by recognizing sequences from the codes. Each code in the compressed data corresponds to a sequence in the dictionary, and these sequences are used to reconstruct the original input.
If a new sequence is encountered (one not yet in the dictionary), the decompressor infers it by using previously decoded sequences. As the dictionary expands during decompression, longer sequences of data can be decoded, effectively restoring the original file
