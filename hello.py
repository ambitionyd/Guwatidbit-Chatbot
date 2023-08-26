import streamlit as st
import processor
st.title("Guwatidbit Chatbot")

if "message" not in st.session_state:
    st.session_state.messages=[]


for message in st.session_state.messages:
    with st.chat_message(message['role']):
        st.markdown(message['content'])


if prompt:=st.chat_input("ask me about IITG"):
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role":"user","content":prompt})

    response=processor.chatbot_response(prompt)

    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role":"assistant",'content':response})
    # st.write(st.session_state.messages)

# def main():
#     # Initialize session state
#     if 'responses' not in st.session_state:
#         st.session_state.responses = []

#     # Display previous responses
#     for response in st.session_state.responses:
#         st.write(response)

#     # User input
#     user_input = st.chat_input("User Input")

#     # Logic to generate bot response
#     bot_response = processor.chatbot_response(user_input)

#     # Store new response in session state
#     if user_input:
#         st.session_state.responses.append(bot_response)

    # if __name__ =="__main__":
    #     main()