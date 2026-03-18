import json
from openai import OpenAI

client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key="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" # Put your new Groq key here
) 

def evaluate_lead(title, description, budget, location):
    print(f"Evaluating lead: '{title}'...")
    
    system_prompt = """
    You are an expert technical sales evaluator. 
    Your job is to read a freelance job lead and score it from 0.0 to 1.0 based on this Ideal Customer Profile:
    - High-end Web Development projects.
    - Budget must be strictly over $2,000.
    
    You must respond ONLY with a valid JSON object in this exact format, with no extra text:
    {
        "score": 0.9,
        "reasoning": "A brief 1-sentence explanation of why."
    }
    """
    
    user_prompt = f"Title: {title}\nDescription: {description}\nBudget: {budget}\nLocation: {location}"

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant", 
        response_format={ "type": "json_object" }, 
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.0 
    )
    
    raw_response = response.choices[0].message.content
    result = json.loads(raw_response)
    
    return result

if __name__ == "__main__":
    dummy_lead_good = {
        "title": "E-commerce Website Redesign",
        "description": "We need a complete overhaul of our Shopify store with custom Python backend integrations.",
        "budget": "$3,500",
        "location": "London, UK"
    }
    
    dummy_lead_bad = {
        "title": "Fix my wordpress menu",
        "description": "The dropdown is broken on mobile, need it fixed ASAP.",
        "budget": "$50",
        "location": "Remote"
    }
    
    print("\n--- Testing Good Lead ---")
    good_result = evaluate_lead(**dummy_lead_good)
    print(json.dumps(good_result, indent=2))
    
    print("\n--- Testing Bad Lead ---")
    bad_result = evaluate_lead(**dummy_lead_bad)
    print(json.dumps(bad_result, indent=2))