from transformers import GPT2Tokenizer

def count_tokens_in_file(file_path):
    # Load pre-trained tokenizer
    tokenizer = GPT2Tokenizer.from_pretrained('gpt2')

    # Read the content of the file
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # Tokenize the text and count the tokens
    tokens = tokenizer.encode(text)
    token_count = len(tokens)  # Get the number of tokens

    return token_count

# Example usage
file_path = 'audio11_chapter_titles.txt'  # Replace with your file path
token_count = count_tokens_in_file(file_path)
print(f"The text file contains {token_count} tokens.")
