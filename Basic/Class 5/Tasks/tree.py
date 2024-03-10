def print_text_pyramid(text):
    max_length = len(text)
    for i in range(max_length):
        padding = " " * (max_length - i - 1)
        partial_text = text[:i+1] + text[:i][::-1]  # Concatenate partial text with its reverse
        print(padding + partial_text + padding)


text = "Every day cars drive around the clock"
print_text_pyramid(text)