import time
import random
from playwright.sync_api import sync_playwright

from brain import evaluate_lead
from voice import generate_pitch

def human_delay(min_seconds=0.1, max_seconds=3.0):
    """Pauses the script for a random amount of time to mimic human hesitation."""
    sleep_time = random.uniform(min_seconds, max_seconds)
    time.sleep(sleep_time)
def run_autonomous_agent():
    print("Initializing Autonomous Lead Agent...")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(
            user_agent="Mozilla/5.0 (WIndow NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome.120.0.0.0 Safari/537.36"
        )
        page = context.new_page()

        try:
            print("\n[1] Navigating to target site...")
            page.goto("https://www.bark.com/en/gb/login/")
            human_delay(2, 4)
            
            print("[2] Demonstrating human-like interaction...")
            email_locator = page.get_by_role("textbox", name="Email")
            email_locator.wait_for(timeout=10000)

            email_locator.click()
            human_delay(0.5, 1.5)
            email_locator.press_sequentially("test_account@example.com", delay=150)

            human_delay(1, 2)

            print("\n[3] Lead detected and extracted.")
            scraped_lead = {
                "title": "Custom Web Application needed",
                "description": "Looking for an expert to build a secure patient portal using React and a Python/FastAPI backend. Needs to integrate with out exsisting PostgreSQL database.",
                "budget": "$4,500",
                "location": "New York, NY"
            }

            human_delay(1,2)

            print("\n[4] Engagint AI Brain for evaluation....")
            evaluation = evaluate_lead(
                scraped_lead["title"],
                scraped_lead["description"],
                scraped_lead["budget"],
                scraped_lead["location"]
            )

            print(f"AI Score: {evaluation['score']}")
            print(f"Resoning: {evaluation['reasoning']}")

            if float(evaluation['score']) > 0.8:
                print("\n[5] Lead approaved. Engaging AI Voice for personlized pitch ... ")
                pitch = generate_pitch(
                    scraped_lead["title"],
                    scraped_lead["description"],
                    scraped_lead["location"]
                )
                print("\n================= Final Deliverable ====================\n")
                print(pitch)
                print("\n==========================================================")
            else:
                print("\n[5] Lead score too low. Discarding and moving to next Lead.")
        except Exception as e:
            print(f"An error occured during automation: {e}")
        
        finally:
            print("\nClosing browser....")
            human_delay(2,3)
            browser.close()

if __name__ == "__main__":
    run_autonomous_agent()