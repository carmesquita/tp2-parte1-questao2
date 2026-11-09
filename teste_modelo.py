from models import load_translation_model, translate_text


model = load_translation_model()

texts = [
    "The cat is on the table.", "Explain what a neural network is.",
    "Students are learning Python and building an application. The application receives English texts and translates them into French. "
    "The teacher explains how to organize the files, create the routes and test the results. "
    "After finishing the project, students write instructions so that another person can install the libraries and run the application."
]

for text in texts:
    print("Texto em inglês:")
    print(text)
    print("")
    print("Tradução:")
    print(translate_text(model, text))

    print("\n--------------------\n")