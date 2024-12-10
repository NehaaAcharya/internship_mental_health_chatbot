# Mental Health Chatbot

This project is a **Mental Health Chatbot** that leverages Natural Language Processing (NLP) and **Logistic Regression** to provide supportive, empathetic conversations for users seeking to manage their mental well-being. Built using **Streamlit**, the chatbot offers personalized responses, tracks emotional states, and logs conversations for future reference. It’s designed to offer a safe, interactive, and engaging experience for users to reflect on their emotions and receive guidance and coping strategies for mental wellness.

---

## Table of Contents

- [About](#about)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [Acknowledgements](#acknowledgements)

---

## About

The **Mental Health Chatbot** uses NLP for understanding user inputs and predicting emotional states, providing personalized responses based on those inputs. The chatbot is powered by **Logistic Regression** for intent classification, and it supports **emotion tracking** through an interactive UI. The bot is designed to guide users in navigating emotions, providing empathetic conversations, mindfulness exercises, and mental health resources.

Key features of the chatbot include:
- Emotion tracking: Helps users identify how they are feeling and suggests coping strategies.
- Conversation history: Stores and displays past interactions, allowing users to reflect on their progress over time.
- Personalized responses: Offers a human-like, empathetic interaction.

---

## Features

- **Emotion Tracking:** Tracks the user’s emotional state and provides tailored advice and strategies based on their mood (Happy, Sad, Angry, etc.).
- **Conversation History:** Stores and displays past interactions, allowing users to reflect on their progress over time.
- **Real-Time Conversations:** Uses a **Logistic Regression model** to classify user input into intents and return relevant responses.
- **Interactive UI:** Built with **Streamlit**, providing an engaging and easy-to-use interface.
- **Customizable Background:** Includes a dynamic background that promotes a soothing and relaxing environment.

---

## Technologies Used

- **Python**: Programming language for developing the chatbot.
- **Natural Language Processing (NLP)**: For understanding user inputs and predicting emotional states.
- **Streamlit**: Framework for building the interactive web interface.
- **scikit-learn**: For intent classification using **Logistic Regression**.
- **NLTK**: Used for tokenizing text and other NLP functionalities.
- **SSL**: To enable secure downloading of NLTK data.
- **CSV**: For logging user conversations.
- **JSON**: For storing intent data and chatbot responses.

---

## Installation

To set up the project locally, follow the steps below:

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/mental-health-chatbot.git
cd mental-health-chatbot
```

### 2. Create a Virtual Environment (Optional, but recommended)

You can create a virtual environment to manage dependencies more effectively.

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### 3. Install Dependencies

Install all the required dependencies listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

---

## Usage

### 1. Run the Application

To run the chatbot application using Streamlit, use the following command:

```bash
streamlit run chatbot.py
```

### 2. Chat with the Bot

- On the home page, choose your current emotional state and start chatting with the bot.
- The bot will respond based on your input and log the conversation for future reference.

### 3. View Conversation History

You can view past conversations by selecting the "Conversation History" option from the sidebar.

---

## Contributing

We welcome contributions to improve this project! If you'd like to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

---

## Acknowledgements

- **NLTK**: For providing essential NLP tools.
- **Streamlit**: For making it easy to build interactive web applications.
- **scikit-learn**: For providing machine learning algorithms for intent classification.
- **Unsplash**: For the beautiful background images used in the UI.
