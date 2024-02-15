input_str = "applepenapplepenpen"
words = ["apple", "pen"]
# input_str = "leetcodecode"
# words = ["leet", "code"]
input_idx = 0
words_idx = 0
input_length = len(input_str)
input_idx_limit = input_length - 1
words_length = len(words)
words_idx_limit = words_length - 1

while input_idx <= input_idx_limit:
    found = False
    while words_idx <= words_idx_limit:
        if input_idx+len(words[words_idx])-1 < len(input_str):
            if input_str[input_idx:input_idx + len(words[words_idx])] == words[words_idx]:
                print("is", input_str[input_idx:input_idx + len(words[words_idx])])
                found = True
                input_idx += len(words[words_idx])
                print("found")
                words_idx = 0
                break  # Break out of the inner loop if a match is found

        words_idx += 1

    if not found:
        print("no match")
        break  # Break out of the outer loop if no match is found



