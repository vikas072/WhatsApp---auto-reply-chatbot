import pyautogui
import pyperclip
import time
from groq import Groq
# from google import genai


client = Groq(api_key=" ")
# client = genai.Client(api_key="AQ.Ab8RN6I-toh_pRduYtTbrSswCskpUz13AQPH_r2gFADOCBjNqA")



def is_last_message_from_sender(chat_log, sender_name="Anant Kho Kho"):
    lines = [line.strip() for line in chat_log.split("\n") if line.strip()]

    if not lines:
        return False

    last_line = lines[-1]

    print("Last line:", last_line)

    return sender_name.lower() in last_line.lower()
    

pyautogui.click(1085, 855)  
time.sleep(1)   

while True:

# Give yourself a moment to switch to the target window
    time.sleep(5)
  
    # Step 2: Drag to select the text
    pyautogui.moveTo(439, 87)
    pyautogui.dragTo(797, 764, duration=2.0, button='left')
    

    # time.sleep(0.5)

    # Step 3: Copy selected text
    pyautogui.hotkey('command', 'c')  # macOS
    # For Windows/Linux use:
    # pyautogui.hotkey('ctrl', 'c')

    time.sleep(2)
    pyautogui.click(469, 394)


    # Step 4: Get text from clipboard into a variable
    chat_history = pyperclip.paste()
 
    print("Copied text:")
    print(chat_history)

    print("condition:",is_last_message_from_sender(chat_history))

    if is_last_message_from_sender(chat_history):
        try:

            print("Calling Groq...")

            responses = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {
                        "role": "system",
                        "content": "You are a person named Vikas who speaks Hindi and English. Output only the next chat reply."
                    },
                    {
                        "role": "user",
                        "content": chat_history
                    }
                ]
            )

            response_text = responses.choices[0].message.content

            print("Generated reply:")
            print(response_text)

            pyperclip.copy(response_text)

            pyautogui.click(553, 792)
            time.sleep(1)

            pyautogui.hotkey('command', 'v')
            time.sleep(1)

            pyautogui.press('enter')
        except Exception as e:
            print("Groq Error:", e)
            continue