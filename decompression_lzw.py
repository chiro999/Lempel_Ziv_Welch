def lzw_decompress(compressed):
    # Initialize dictionary with single characters (ASCII 0-255)
    dict_size = 256
    dictionary = {i: chr(i) for i in range(dict_size)}
    
    w = chr(compressed.pop(0))  # First code -> initial string
    decompressed_data = [w]  # Decompressed output

    # Iterate over compressed data
    for k in compressed:
        if k in dictionary:
            entry = dictionary[k]  # Get string from dictionary
        elif k == dict_size:
            entry = w + w[0]  # Special case: infer new sequence
        else:
            raise ValueError(f"Bad compressed k: {k}")

        decompressed_data.append(entry)  # Append decoded string

        # Add new sequence to dictionary
        dictionary[dict_size] = w + entry[0]
        dict_size += 1

        w = entry  # Update current sequence
    
    return ''.join(decompressed_data)
