from openai import OpenAI

client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key="" #I have removed my API key for security reasons
)

def generate_pitch(title, description, location):
    print(f"Generating personalized pitch for: '{title}'...\n")

    system_prompt = """
    Your are an elite, highly presuasive freelance software engineer bidding on a project .
    Your goal is to write a highly converting, confident, and professional email pitch.

    Strict Constraints:
    1. The pitch Must be exactly 3 pragraphs long.
    2. You must seamlessly reference at least two specific details from the clients's job description to prove you actually read it.
    3. Do not use robotic corporate jargon. Sound like a competentm high-end professional human.
    4. Do not include subject lines or placeholder brackets like [Your Name]. Just write the body of the email.
    """

    user_prompt = f"Job Title: {title}\nJob Description: {description}\nClient Location: {location}\n\nWrite the pitch."

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content":system_prompt},
            {"role": "user", "content":user_prompt}
        ],
        temperature=0.7
    )

    pitch = response.choices[0].message.content
    return pitch

if __name__ == "__main__":
    dummy_lead_good = {
        "title": "E-commerce Website Redesign",
        "description": "We need a complete overhaul of our SHopify store with custom Python backend integration.",
        "location": "London, UK"
    }

    final_pitch = generate_pitch(
        title=dummy_lead_good["title"],
        description=dummy_lead_good["description"],
        location=dummy_lead_good["location"]
    )

    print("=== DRAFTED PITCH ===\n")
    print(final_pitch)
    print("\n=====================")
