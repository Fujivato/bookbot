def main():
    filename = "books/frankenstein.txt"
    text = get_book_text(filename)
    generate_analysis_report(filename, text)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words_in_text(text):
    words = text.split()
    return len(words)

def count_characters_in_text(text):
    character_counts = {}
    
    for char in text:
        lowered = char.lower()
        if lowered not in character_counts:
            character_counts[lowered] = 1
        else:
            character_counts[lowered] += 1
    
    return character_counts

def generate_analysis_report(filename, text):
    print(f"--- Begin report of {filename} --- ")
    
    #add  header for word count
    word_count = count_words_in_text(text)
    print(f"{word_count} words found in the document")
    print("")
    
    # write out character counts
    character_counts = count_characters_in_text(text)
    for character in character_counts:
        character_clean = character.strip('\r\n') # strip \r\n from output to avoid newlines being printed into console
        print(f"The '{character_clean}' chracter was found {character_counts[character]} times")    
        pass
    
    print("--- End report ---")
    
main()
