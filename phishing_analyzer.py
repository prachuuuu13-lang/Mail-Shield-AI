import os
from groq import Groq

SYSTEM_PROMPT = """You are a cybersecurity expert specialising in phishing email detection.

when a user gives you an email to analyse,you must check:
1.SENDER DOMAIN - Is the domain legitimate or fake or spoofed?
2.PSYCHOLOGICAL LEVERS - Does it use urgency,authority,or curiosity?
3.SUSPICIOUS LINKS - Does visible text match the actual destination?
4.THE ASK - Does it ask you to click something urgently?

Respond in this exact format:

VERDICT:[PHISHING/LEGITIMATE/SUSPICIOUS]

SENDER ANALYSES:
[Your analyses of the sender domain]

PSYCHOLOGICAL LEVER DETECTED:
[List which levers-urgency/authority/curiosity]

RED FLAGS FOUND:
[List specific red flags]

RECOMMENDATION:
[What the user should do]"""

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))


def get_multiline_input():
    print("enter the email content (type 'END' on a line by itself to finish or quit to exit)")
    lines = []
    while True:
        line = input()
        if line.strip().upper() == "END":
            break
        if line.strip().lower() == "quit":
            return None
        lines.append(line)
    return "\n".join(lines)


email_content = get_multiline_input()
if email_content is None:
    exit()
print("\n"+"="*60)
print("ANALYSING EMAIL PLEASE WAIT 🤔🤔🤔🤔\n")
print("="*60)
response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": f"Analyze the following email for phishing:\n\n{email_content}"}
    ],
    max_tokens=1000
)
print("="*60)
print("\nANALYSIS COMPLETE ✅\n")
print("="*60)
print(response.choices[0].message.content)
