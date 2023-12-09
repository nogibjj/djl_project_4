# Project 4 Shakespeare Poem Generator Flask APP
Visit the app: [shakespearepoemgenerator.azurewebsites.net](shakespearepoemgenerator.azurewebsites.net)

This project is a web-based application that generates Shakespearean poems based on user-selected phrases. The application is built using Flask and can be easily deployed using Docker and Azure App Services. 

The poems in the Shakespeare Poem Generator are generated using the Hugging Face Transformers library, which leverages pre-trained language models. Specifically, the generator uses the GPT-2 (Generative Pre-trained Transformer 2) model.

1. GPT-2 Model: The core of the poem generation is the GPT-2 language model. GPT-2 is a type of transformer model, which is a neural network architecture known for its effectiveness in natural language processing tasks.
2. Prompting: When a user clicks on one of the provided Shakespearean phrases, it serves as a prompt for the GPT-2 model. The selected phrase acts as the initial input to the model, guiding it to generate coherent and contextually relevant text.
3. Text Generation: The GPT-2 model generates a continuation of the given prompt, producing a sequence of text that extends the user-provided phrase into a full poem. The model's training on a diverse range of text data allows it to capture the style and language of William Shakespeare.

**It's important to note that the quality and style of the generated poems heavily depend on the training data of the GPT-2 model. GPT-2 has been trained on a diverse range of internet text, including literary works, which allows it to mimic various writing styles, including that of William Shakespeare. The model's ability to capture context and generate coherent text makes it well-suited for creative text generation tasks like poem writing.** 

<img width="1710" alt="Screenshot 2023-12-08 at 11 42 15 PM" src="https://github.com/nogibjj/djl_project_4/assets/143829673/36d3cc84-f2cb-401c-9710-714a17da4a86">



## Project Structure

├── Dockerfile
├── Makefile
├── README.md
├── __pycache__
│   └── app.cpython-38.pyc
├── app.py
├── requirements.txt
├── static
│   └── shakespeare.png
└── templates
    └── index.htm


## Deployment  on Azure App Services:




## YouTube Demo

Watch the demo video on YouTube:

## Conclusion and Recommendations

This project demonstrates the use of Flask for building a web-based application and Docker for containerization. The application's simplicity allows for easy deployment on various platforms, such as Azure App Services.

Recommendations:
- Consider trainig the model on Shakespeare texts for more accurete poems
- Consider implementing additional features or integrations to enhance the application.
Continuously monitor and optimize the application's performance in a production environment.
