from openai import OpenAI
import os
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


# Ensure your OpenAI API key is correctly set in your environment variables

def read_transcript_from_file(file_path):
    """
    Reads the transcript text from a given file path.
    
    Args:
    - file_path (str): Path to the transcript file.
    
    Returns:
    - str: The content of the transcript.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        transcript = file.read()
    return transcript

def generate_learning_activities(transcript):
    """
    Sends a transcript to ChatGPT to generate ideas for fun learning activities.
    
    Args:
    - transcript (str): The text of the video transcript.
    
    Returns:
    - str: Ideas for learning activities based on the transcript.
    """
    prompt_text = transcript[:min(len(transcript), 2048)]  # Adjust based on your token budget
    messages = [{
        "role": "system",
        "content": "You are a helpful assistant."
    },{
        "role": "user",
        "content": f"Given the following transcript from a children's educational video, identify key educational themes and suggest fun learning activities that can be developed for kids aged 4-8 years old. Focus on activities that promote engagement, creativity, and learning.\n\nTranscript: \"{prompt_text}\""
    }]
    
    response = client.chat.completions.create(model="gpt-4-turbo-preview",  # Specify the model you're using; adjust as needed
    messages=messages,
    temperature=0.5,
    max_tokens=150,  # Adjust based on the desired detail of response and token budget
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0)
    
    # Extracting text from the last message in response
    if response.choices and len(response.choices) > 0:
        last_message = response.choices[0].message.content
        return last_message.strip()
    else:
        return "No activities could be generated."

def main(file_path):
    """
    Main function to orchestrate the process of reading a transcript and generating learning activities.
    
    Args:
    - file_path (str): Path to the transcript file.
    """
    transcript = read_transcript_from_file(file_path)
    activities = generate_learning_activities(transcript)
    print("Suggested Learning Activities:\n", activities)

if __name__ == "__main__":
    file_path = "output_1_new.txt"  # Update this to the path of your transcript file
    main(file_path)
