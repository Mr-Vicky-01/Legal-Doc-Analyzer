# Legal Doc Analyzer 📄

## Overview

Legal Doc Analyzer is a web application that uses AI to analyze legal documents and provide responses based on user prompts. It utilizes the Gemini model from Google Generative AI to generate content and offers a user-friendly interface for interacting with the model. This project demonstrates the application of AI in the legal field, making it a valuable addition to your portfolio.

## Features

- Analyze legal documents using the Gemini model.
- Generate responses based on user prompts.
- User-friendly interface for interaction.

## Demo

Try this app: [Link](https://huggingface.co/spaces/Mr-Vicky-01/Legal-Doc-Analyzer)

![image](https://github.com/Mr-Vicky-01/Legal-Doc-Analyzer/assets/143078285/ab6d6be4-8146-4203-ab50-656078d30b2c)


## Getting Started

### Prerequisites

- Python 3.x
- Google Generative AI (`google-generativeai`)
- Required Python libraries (listed in `requirements.txt`)

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Mr-Vicky-01/Legal-Doc-Analyzer.git
    cd Legal-Doc-Analyzer
    ```

2. Install the required libraries:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

3. Set up the Google API Key:

    Go to this site to generate API key [HERE](https://aistudio.google.com). Once you have the API key, locate the .env file in your project directory. Open it and paste your API key like this:
    ```bash
    GOOGLE_API_KEY = "paste the api key here"
    ```

### Usage

1. Run the application:
    ```bash
    python app.py
    ```

2. Interact with the app by providing prompts and optionally uploading images.

## File Structure

- `app.py`: Main application file.
- `requirements.txt`: Lists the required Python packages for the application.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Contact

For any questions or feedback, feel free to reach out:

- **Email**: pachaiappan1102@gmail.com

## Acknowledgments

- Gemini API for their powerful content generation model.
- The open-source community for providing valuable resources and support.
