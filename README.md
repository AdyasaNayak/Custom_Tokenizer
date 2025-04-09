# Custom Tokenizer

A simple character-level tokenizer implemented in Python. This tokenizer assigns a unique ID to each character from a predefined set, and allows for both tokenization and detokenization of text.

## Features

- Tokenizes text into character-level token IDs.
- Detokenizes token IDs back to the original text.
- Supports common English letters, punctuation, symbols, whitespace, and control characters like `\n` and `\t`.

## Usage

### Example

```python
tokenizer = CustomTokenizer()
text = input("Enter a sample text: ")
tokens = tokenizer.tokenize(text)
print("Tokenization:", tokens)
og_text = tokenizer.detokenize(tokens)
print("Detokenization:", og_text)
