import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os
from datetime import datetime

# Load environment variables
load_dotenv()

class GeminiChatbot:
    def __init__(self):
        api_key = os.getenv('GEMINI_API_KEY')
        if not api_key:
            raise ValueError("GEMINI_API_KEY not found in environment variables")
        
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('models/gemini-2.5-flash')
        
    def get_response(self, message, history):
        """Get response from Gemini"""
        try:
            # Create chat with history
            chat = self.model.start_chat(history=history)
            response = chat.send_message(message)
            return response.text
        except Exception as e:
            return f"Error: {str(e)}"

def main():
    st.set_page_config(
        page_title="Gemini Chatbot",
        page_icon="🤖",
        layout="wide"
    )
    
    st.title("🤖 Gemini Chatbot")
    st.markdown("---")
    
    # Initialize chatbot
    try:
        if 'chatbot' not in st.session_state:
            st.session_state.chatbot = GeminiChatbot()
        
        # Initialize chat history
        if 'messages' not in st.session_state:
            st.session_state.messages = []
        
        # Display chat history
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
        
        # Chat input
        if prompt := st.chat_input("What would you like to know?"):
            # Add user message to chat history
            st.session_state.messages.append({"role": "user", "content": prompt})
            
            # Display user message
            with st.chat_message("user"):
                st.markdown(prompt)
            
            # Get bot response
            with st.chat_message("assistant"):
                with st.spinner("Thinking..."):
                    # Convert history to Gemini format
                    history = []
                    for msg in st.session_state.messages[:-1]:
                        role = "user" if msg["role"] == "user" else "model"
                        history.append({"role": role, "parts": [msg["content"]]})
                    
                    response = st.session_state.chatbot.get_response(prompt, history)
                    st.markdown(response)
            
            # Add assistant response to chat history
            st.session_state.messages.append({"role": "assistant", "content": response})
        
        # Sidebar
        with st.sidebar:
            st.header("Options")
            
            if st.button("Clear Chat History"):
                st.session_state.messages = []
                st.rerun()
            
            if st.button("Export Conversation"):
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = f"conversation_{timestamp}.txt"
                
                with open(filename, 'w', encoding='utf-8') as f:
                    for msg in st.session_state.messages:
                        f.write(f"{msg['role'].upper()}: {msg['content']}\n\n")
                
                st.success(f"Conversation exported to {filename}")
            
            st.markdown("---")
            st.markdown("### About")
            st.info("This chatbot uses Google's Gemini Pro model to provide intelligent responses.")
    
    except Exception as e:
        st.error(f"Error initializing chatbot: {str(e)}")
        st.info("Please make sure your GEMINI_API_KEY is set in the .env file")

if __name__ == "__main__":
    main()