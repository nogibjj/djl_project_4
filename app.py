from flask import Flask, render_template, request
from transformers import pipeline
import re

app = Flask(__name__)

# GPT-2 text generation pipeline
generator = pipeline('text-generation', model='gpt2')

# Shakespeare phrases for buttons
shakespeare_phrases = [
"I do love nothing in the world so well as you—is not that strange?",
"My bounty is as boundless as the sea, My love as deep. The more I give to thee,The more I have, for both are infinite.",
"Thy sweet love remembered such wealth brings That then I scorn to change my state with kings"
"I kiss thee with a most constant heart.",
"A heaven on earth I have won by wooing thee.",
"When you do dance, I wish you, A wave o’ th’ sea, that you might ever do Nothing but that. . .",
"So are you to my thoughts as food to life,Or as sweet-seasoned showers are to the ground.",
"I would not wish any companion in the world but you.Thee will I love, and with thee lead my life.",
"The course of true love never did run smooth.If music be the food of love, play on.",
"Give me excess of it, that, surfeiting,The appetite may sicken and so die.",
"Love is a smoke rais’d with the fume of sighs;Being purg’d, a fire sparkling in a lover’s eyes;",
]


# Home route
@app.route('/', methods=['GET', 'POST'])
def home():
    generated_poem = None

    if request.method == 'POST':
        # Get the selected Shakespeare phrase from the form
        selected_phrase = request.form.get('shakespeare_phrase')

        # Generate a new poem using the selected phrase
        generated_poem = generate_poem_from_prompt(selected_phrase)

    return render_template('index.html', phrases=shakespeare_phrases, generated_poem=generated_poem)

# Function to generate a poem based on a prompt
def generate_poem_from_prompt(prompt):
    generated_poem = generator(prompt, max_length=150, num_return_sequences=1)

    # Extract generated text and remove the input phrase
    generated_text = generated_poem[0]['generated_text'][len(prompt):].strip()

    # Add line breaks after punctuation marks and commas
    formatted_poem = re.sub(r'(?<=[.,;!?])', '\n', generated_text)

    return formatted_poem

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)