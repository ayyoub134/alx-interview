def validUTF8(data):
    # Number of bytes in the current UTF-8 character
    num_bytes = 0
    
    # Masks to identify the leading bits of a byte
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000
    
    for byte in data:
        # Get only the least significant 8 bits
        byte = byte & 0xFF
        
        if num_bytes == 0:
            # Count the number of leading 1's in the byte
            mask = 1 << 7
            while mask & byte:
                num_bytes += 1
                mask >>= 1
            
            # 1-byte characters (0xxxxxxx) or invalid case
            if num_bytes == 0:
                continue
            if num_bytes == 1 or num_bytes > 4:
                return False
            
        else:
            # Check if the current byte is a valid continuation byte (10xxxxxx)
            if not (byte & mask1 and not (byte & mask2)):
                return False
        
        # We process one less byte to expect
        num_bytes -= 1
    
    # If num_bytes is not 0, there are incomplete characters
    return num_bytes == 0

