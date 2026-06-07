from word_counter2 import*


def analyze_text(text): 
    cleaned_txt= process(text)
    words= to_words(cleaned_txt)
    total_words=len(words)
    unique_words= num_of_uniques(cleaned_txt)
    avg_word_length= average_word_length(cleaned_txt)
    Lexical_diversity= lexical_diversity(cleaned_txt)
    print(f'TEXT ANALYSIS REPORT\n---------------------\n\
        total wrds={total_words}\nunique words = {unique_words}\n\
        avrage word length = {avg_word_length}\n \
        lexical diversity = {Lexical_diversity}\n')


text = input("enter a text : \n")


analyze_text(text)
