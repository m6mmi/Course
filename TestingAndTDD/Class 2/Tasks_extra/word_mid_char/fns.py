def get_middle(text):
    # (len(text) - 1) // 2 --> Get start position
    # (len(text) + 2) // 2 --> Get end position
    return text[(len(text) - 1) // 2:(len(text) + 2) // 2]
