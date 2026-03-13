import gradio as gr

def rule_based_chatbot(message: str) -> str:
    """
    A very simple rule-based chatbot.
    Adjust or extend rules as you like.
    """

    if not message:
        return "I didn't catch that. Could you type something?"

    # lowercase for easier matching
    text = message.lower().strip()

    # Greeting rules
    if any(word in text for word in ["hello", "hi", "hey", "good morning", "good evening"]):
        return "Hi there! 👋 How can I help you today?"

    # Goodbye rules
    if any(word in text for word in ["bye", "goodbye", "see you", "cya"]):
        return "Goodbye! Thanks for chatting with me. 😊"

    # Simple FAQ-style rules
    if "your name" in text:
        return "I'm a simple rule-based chatbot built in Python and Gradio 🤖."

    if "help" in text or "what can you do" in text:
        return (
            "I’m a simple demo chatbot. I can respond to greetings, say goodbye, "
            "and answer a few basic questions. Try saying 'hello' or 'what is your name?'"
        )

    if "time" in text:
        return "I don't actually know the time yet ⏰, but you could teach me later!"

    # Default / fallback
    return (
        "I'm not sure how to respond to that yet. 🤔\n"
        "Try asking me things like:\n"
        "- 'hello'\n"
        "- 'what is your name?'\n"
        "- 'help'\n"
        "- 'bye'"
    )

# Create Gradio interface
chat_interface = gr.Interface(
    fn=rule_based_chatbot,      # function to call
    inputs=gr.Textbox(
        lines=2,
        placeholder="Type your message here..."
    ),
    outputs="text",
    title="Simple Rule‑Based Chatbot",
    description="A demo chatbot built with Python and Gradio.",
)

if __name__ == "__main__":
    # launch the Gradio app
    chat_interface.launch()
