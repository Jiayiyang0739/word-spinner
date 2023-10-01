import string
from Spinner import Spinner

def main():
    # Load Spinner with the test synonyms
    spinner = Spinner('test-synonyms.txt')

    # Read essay.txt
    with open('essay.txt', 'r') as file:
        text = file.read().lower()
        # Remove punctuation
        text = text.translate(str.maketrans('', '', string.punctuation))

    # Print the original
    print("Original :", text)

    # Print three spun versions
    for i in range(3):
        spun_text = spinner.spin_text(text)
        print(f"Option {i + 1} :", spun_text)

if __name__ == "__main__":
    main()