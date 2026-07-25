import random
def build_mark_of_chain(text):
    words = text.split()
    chain = {}
    for i in range(len(words) - 1):
        current , next_word = words[i], words[i + 1]
        chain.setdefault(current, []).append(next_word)
    return chain

def generate_text(chain, length=30):
     word = random.choice(list(chain.keys()))
     result = [word]
     for _ in range(length - 1):
         next_words = chain.get(word)
         if not next_words:
             break
         word = random.choice(next_words)
         result.append(word)
         if not next_words:
            word = random.choice(list(chain.keys()))
         else:
            word = random.choice(next_words)
            result.append(word)
            return ' '.join(result)      
        
##trying to build a Markov chain from the given text
text = ""
"This is a sample text for building a Markov chain. The Markov chain will generate random text based on the input text ."
""