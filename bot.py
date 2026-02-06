import pyautogui
import time
import pyperclip
from groq import Groq

client = Groq(
    api_key="my_api_key", #customize it by your API key
)
def is_last_msg_from_sender(chat_log,sender_name="Modi Psit"): 
    messages = chat_log.strip().split("`26] ")[-1]
    if sender_name in messages:
        return True
    return False

pyautogui.click(697, 1045)
time.sleep(1)

while True:
    pyautogui.moveTo(706, 250)
    pyautogui.dragTo(1866, 921, duration=1.0, button="left")  # Select chat text

    pyautogui.hotkey("ctrl", "c")  # Copy selected text
    time.sleep(2)
    pyautogui.click(1766, 820)

    text = pyperclip.paste()

    print(text)
    if is_last_msg_from_sender(text):

        completion = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=[
                {
                    "role": "system",
                    "content": "You are a person named Saksham who speaks Hindi as well as English.You are from India and is a Python coder and Tech enthusiast and loves to watch movies of different jaunra. You analyze chat history and respond like Saksham.",
                },
                {"role": "user", "content": text},
            ],
            temperature=1,
            max_completion_tokens=8192,
            top_p=1,
            reasoning_effort="medium",
            stream=False,
            stop=None,
        )

        response = completion.choices[0].message.content or ""
        pyperclip.copy(response)

        pyautogui.click(1266, 975)  # Click input field again to ensure focus
        time.sleep(1)

        pyautogui.hotkey("ctrl", "v")
        time.sleep(1)

        pyautogui.press("enter")
