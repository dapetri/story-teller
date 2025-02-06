import datetime
import os
from pathlib import Path
import random
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")


def generate_story():
    seed = random.randint(0, 10000)

    prompt = f"""Give me a horrible and chilling fact about our worlds. Seed: {seed}"""
    horrible_fact = model.generate_content(prompt).text

    prompt = f"""Base a story on the following horrible fact: {horrible_fact}. The story should follow an event that really happened. 
    The story should be told in the third person and use simple language. Add gore and adult content. Focus on building suspense and fear through details, unexplained phenomena, 
    and a chilling climax. The story should keep the listener engaged and unsettled from beginning to end. Seed: {seed}"""
    #### End of Prompting ####

    response = model.generate_content(prompt)

    # Setup file saving
    folder_path = os.path.join("src", "res", "txt")
    file_path = os.path.join(
        folder_path, f"{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    )

    # Create directory if it doesn't exist
    os.makedirs(folder_path, exist_ok=True)

    # Save the story
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(response.text)

    return response.text


def generate_tiktok_description(story: str):
    # Generate TikTok description
    desc_prompt = f"""Write a catchy TikTok description for the following horror story. 
    The description should be short, engaging, and catchy.
    Include relevant hashtags to attract a horror-loving audience. 
    Story: {story}"""

    desc = model.generate_content(desc_prompt).text

    # Setup description file saving
    desc_folder_path = os.path.join("src", "res", "desc")
    desc_file_path = os.path.join(
        desc_folder_path, f"{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    )

    # Create directory if it doesn't exist
    os.makedirs(desc_folder_path, exist_ok=True)

    # Save the TikTok description
    with open(desc_file_path, "w", encoding="utf-8") as f:
        f.write(desc)


if __name__ == "__main__":
    story = generate_story()
    generate_tiktok_description(story)
