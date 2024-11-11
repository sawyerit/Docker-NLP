from summarizer import Summarizer
from bs4 import BeautifulSoup

# Sample text - "Artificial intelligence (AI) is a branch of computer science that aims to create machines capable of intelligent behavior. These machines are designed to mimic human cognitive functions such as learning, problem-solving, and decision-making. AI technologies can be classified into two main types: narrow or weak AI, which is designed for a particular task, and general or strong AI, which possesses the ability to understand, learn, and apply knowledge across various domains. One of the most popular approaches in AI is machine learning, where algorithms are trained on large datasets to recognize patterns and make predictions."

if __name__ == "__main__":
    while True:
        input_text = input("Enter the text for summarization (type 'exit' to end): ")

        if input_text.lower() == 'exit':
            print("Exiting...")
            break

        bert_model = Summarizer()
        soup = BeautifulSoup(input_text, "html.parser")

        #preserve some formatting so text doesn't get smashed together
        for tag in soup.find_all(['br', 'p']):
            tag.replace_with(' ' + tag.get_text() + ' ')
        
        # remove multiple spaces
        clean_text = " ".join(soup.get_text().split())
        summary = bert_model(clean_text)
 
        print(summary)
