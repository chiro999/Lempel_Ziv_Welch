def lzw_compress(uncompressed):
    # Initialize dictionary with single character strings (ASCII 0-255)
    dict_size = 256
    dictionary = {chr(i): i for i in range(dict_size)}
    
    w = ""  # Current sequence
    compressed_data = []  # Compressed output (list of codes)

    # Iterate over input string
    for c in uncompressed:
        wc = w + c  # Build new sequence
        if wc in dictionary:
            w = wc  # Continue building sequence
        else:
            compressed_data.append(dictionary[w])  # Output code for current sequence
            dictionary[wc] = dict_size  # Add new sequence to dictionary
            dict_size += 1  # Increment dictionary size
            w = c  # Start new sequence

    # Output the last sequence
    if w:
        compressed_data.append(dictionary[w])
    
    return compressed_data
