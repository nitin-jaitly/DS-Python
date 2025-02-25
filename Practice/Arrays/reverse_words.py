def reverse_characters_in_a_word(word, left_index, right_index):
     while left_index <= right_index:
         word[left_index], word[right_index] = word[right_index], word[left_index]
         left_index += 1
         right_index -= 1
     return word

def reverse_words(message):
    reverse_characters_in_a_word(message,0, len(message) - 1)
    # This will be the index of the start of the current word
    current_word_start_index = 0

    # We will go through the entire message and reverse each word
    for i in range(len(message) + 1 ):
        # If we reach the end of the message or we reach a space, we reverse the current word
        if i == len(message) or message[i] == ' ':
            reverse_characters_in_a_word(message, current_word_start_index,i - 1)
            current_word_start_index = i + 1
    return message

def main():
    message = [ 'c', 'a', 'k', 'e', ' ',
            'p', 'o', 'u', 'n', 'd', ' ',
            's', 't', 'e', 'a', 'l' ]

    print(reverse_words(message))


if __name__ == "__main__":
    main()
