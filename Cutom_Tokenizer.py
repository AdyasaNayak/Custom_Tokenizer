class CustomTokenizer:
    def __init__(self):
        chars = ("abcdefghijklmnopqrstuvwxyz" + "ABCDEFGHIJKLMNOPQRSTUVWXYZ" + "!@#$%^&*()_-+=[]{ }|;:',.<>?/~`\"\\\n \t")
        self.char_to_index = {c: i+1 for i, c in enumerate(chars)}
        self.index_to_char = {i+1: c for i, c in enumerate(chars)}
        
    def tokenize(self, text):
        token_IDs = []
        for char in text:
            if char in self.char_to_index:
                token_IDs.append(self.char_to_index[char])  
            else:
                print(f"Unknown character !")
        return token_IDs
    
    def detokenize(self, token_IDs):
        chars = []
        for tid in token_IDs:
            if tid in self.index_to_char:
                chars.append(self.index_to_char[tid])
            else:
                print(f"Unknown token id !")
        return ''.join(chars)
    

tokenizer = CustomTokenizer()
text = input("Enter a sample text :")
tokens = tokenizer.tokenize(text)
print("Tokenization : ",tokens)
og_text = tokenizer.detokenize(tokens)
print("Detokenization : ", og_text) 