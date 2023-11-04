# Extractive Text Summarizer

## Overview
The Extractive Text Summarizer is a web-based tool that condenses lengthy articles, papers, or documents into a user-defined number of informative sentences. Utilizing natural language processing (NLP) techniques, the summarizer identifies and extracts key sentences, providing a coherent and concise summary.

## Features
- **Custom Summary Length**: Users can define the exact number of summary lines.
- **Text Input**: A simple interface for pasting the text to be summarized.
- **Responsive Design**: A clean, responsive UI that adapts to different screen sizes.
- **Fast Processing**: Quick text analysis and summarization.

## Tech Stack
- **Python**: Backend programming language.
- **NLP**: Techniques for processing and analyzing natural language data.
- **Flask**: Lightweight web application framework.
- **HTML5**: Standard markup language for creating web pages.
- **CSS3**: Style sheet language used for describing the presentation of a document.

## Getting Started

### Prerequisites
- Python 3.6+
- Pip package manager

### Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/<your-username>/extractive-text-summarizer.git```

2. Navigate to the project directory:
   ```sh
   cd extractive-text-summarizer```

4. Install the required packages:
   ```sh
   pip install -r requirements.txt```

### Running the Application
1. Start the Flask server.
2. Open your web browser and navigate to `http://127.0.0.1:5000/`.
3. Paste the text you want to summarize in the provided text area.
4. Enter the number of lines for the summary.
5. Click on the "Summarize" button to get the summary.

## How It Works
The application uses an extractive summarization algorithm which:
- Tokenizes the input text into sentences.
- Ranks sentences based on their significance using NLP techniques.
- Extracts the top-ranked sentences based on the user-specified summary length.




   
