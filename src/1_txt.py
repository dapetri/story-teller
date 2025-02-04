import datetime
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

#### Propting ####
current_time = datetime.datetime.now()
time_of_day = current_time.strftime("%H:%M")
current_date = current_time.strftime("%B %d")
day_period = "morning" if 5 <= current_time.hour < 12 else "afternoon" if 12 <= current_time.hour < 17 else "evening" if 17 <= current_time.hour < 21 else "night"

prompt = f"""Write a psychological horror story between 400-500 words that takes place on {current_date} at {time_of_day} during the {day_period}. 

Requirements:
- Build tension gradually
- Include atmospheric details about the time of day and date
- Focus on psychological fear rather than gore
- Create a distinct beginning, middle, and end
- End with an unsettling twist
- Keep descriptions vivid but concise
- Make both the {day_period} and the date {current_date} crucial to the story
- Use first-person perspective
- Maintain a sense of dread throughout
- Incorporate any significant cultural or seasonal aspects of {current_date}

The story should make readers feel unsafe during this particular time of {day_period} and make them dread this specific date."""
#### End of Prompting ####

model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content(prompt)

# Setup file saving
folder_path = os.path.join("src","res", "txt")
file_path = os.path.join(folder_path, f"{current_time.strftime('%Y%m%d_%H%M%S')}.txt")

# Create directory if it doesn't exist
os.makedirs(folder_path, exist_ok=True)

# Save the story
try:
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(response.text)
    print(f"Story saved to: {file_path}")
except Exception as e:
    print(f"Error saving story: {e}")