import os
import json
import datetime
import csv
import nltk
import ssl
import streamlit as st
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# SSL setup for NLTK
ssl._create_default_https_context = ssl._create_unverified_context
nltk.download('punkt')

# Load intents from the JSON file
file_path = os.path.abspath("./intents.json")
with open(file_path, "r") as file:
    intents = json.load(file)

# Create the vectorizer and classifier
vectorizer = TfidfVectorizer(ngram_range=(1, 3))  # Adjust n-grams for better feature extraction
clf = LogisticRegression(random_state=0, max_iter=10000)

# Preprocess the data
tags = []
patterns = []
for intent in intents:
    for pattern in intent['patterns']:
        tags.append(intent['tag'])
        patterns.append(pattern)

# Training the model
x = vectorizer.fit_transform(patterns)
y = tags
clf.fit(x, y)

# Chatbot function
def chatbot(input_text):
    # Preprocess the input text
    input_text = input_text.lower()
    input_vector = vectorizer.transform([input_text])

    # Predict the intent tag
    tag = clf.predict(input_vector)[0]

    # Find responses for the predicted tag
    for intent in intents:
        if intent['tag'] == tag:
            response = random.choice(intent['responses'])
            return response, tag

    # Default fallback response
    return "I'm sorry, I didn't understand that. Could you please rephrase?", "unknown"

# Function to add custom background
def add_bg_from_url():
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("https://source.unsplash.com/1600x900/?mental,health");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Streamlit main function
def main():
    # Add custom background
    add_bg_from_url()
    
    st.title("🌼 Mental Health Chatbot")
    
    # Sidebar Menu
    menu = ["🏠 Home", "📜 Conversation History", "ℹ️ About"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "🏠 Home":
        st.write("Hello! I am your mental health assistant. How are you feeling today?")
        
        # Add emotion selector
        emotion = st.selectbox(
            "How are you feeling today?",
            ["😊 Happy", "😟 Sad", "😡 Angry", "😰 Stressed", "🤔 Curious"]
        )
        st.write(f"You're feeling {emotion.split()[1]}! Let's talk about it.")

        # Ensure chat log file exists
        if not os.path.exists('chat_log.csv'):
            with open('chat_log.csv', 'w', newline='', encoding='utf-8') as csvfile:
                csv_writer = csv.writer(csvfile)
                csv_writer.writerow(['User Input', 'Chatbot Response', 'Predicted Tag', 'Timestamp'])

        user_input = st.text_input("You:")
        if user_input:
            response, tag = chatbot(user_input)
            response = f"😊 {response}" if tag != "unknown" else f"🤔 {response}"
            st.text_area("Chatbot:", value=response, height=120, max_chars=None)

            # Log the conversation
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open('chat_log.csv', 'a', newline='', encoding='utf-8') as csvfile:
                csv_writer = csv.writer(csvfile)
                csv_writer.writerow([user_input, response, tag, timestamp])

            # Display debugging information
            st.write(f"**Debug Info:** Predicted Tag - {tag}")

            if response.lower() in ['goodbye', 'bye']:
                st.write("Thank you for chatting. Have a great day! 🌟")
                st.stop()

            # Feedback button
            if st.button("Was this helpful? 👍 / 👎"):
                st.write("Thank you for your feedback! 😊")

    elif choice == "📜 Conversation History":
        st.header("📜 Conversation History")
        if os.path.exists('chat_log.csv'):
            with open('chat_log.csv', 'r', encoding='utf-8') as csvfile:
                csv_reader = csv.reader(csvfile)
                next(csv_reader)  # Skip header
                for row in csv_reader:
                    st.markdown(f"""
                    <div style="background-color: #f0f2f6; padding: 10px; border-radius: 5px; margin-bottom: 10px;">
                        <strong>User:</strong> {row[0]}<br>
                        <strong>Chatbot:</strong> {row[1]}<br>
                        <small><em>{row[3]}</em></small>
                    </div>
                    """, unsafe_allow_html=True)
        else:
            st.write("No conversation history available.")

    elif choice == "ℹ️ About":
        st.write("Hi! I am an intents-based chatbot powered by **Natural Language Processing (NLP)** and **Logistic Regression** for intent classification, designed to support your mental health journey through meaningful and empathetic conversations. I provide features like emotion tracking to help you identify and express your feelings, secure conversation logging for revisiting past interactions, and a user-friendly interface powered by Streamlit for a seamless experience. Additionally, I offer educational insights on mental health concepts, coping strategies, and mindfulness techniques, ensuring an engaging and supportive dialogue. Continuously improving based on user interactions, I adapt to provide personalized support, creating a safe and helpful space for self-reflection and emotional well-being. Let’s talk! 🌸✨")

if __name__ == '__main__':
    main()
