from openai import OpenAI
import os
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_lecture_on_topic(topic):
    """
    Uses a given topic to generate a new lecture outline or detailed content using the ChatGPT API.
    """
    messages = [
        {
            "role": "system",
            "content": "You are a helpful lecture generator. Your task is to create an informative and engaging lecture outline or full lecture content based on the provided topic. Include key points, detailed explanations, relevant examples, questions for the audience, and any practical activities that can help in understanding the topic. Also, structure the lecture to flow logically from introduction to conclusion."
        },
        {
            "role": "user",
            "content": f"Generate a lecture on the following topic: {topic}"
        }
    ]

    response = client.chat.completions.create(
        model="gpt-4-turbo-preview",
        messages=messages,
        temperature=0.5,
        max_tokens=2000,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    
    if response.choices and len(response.choices) > 0:
        lecture_content = response.choices[0].message.content
        return lecture_content.strip()
    else:
        return "Unable to generate lecture content."

def write_output_to_file(lecture_content, output_file_path):
    """
    Writes the generated lecture content to a specified text file.
    
    Args:
    - lecture_content (str): The generated lecture content to write.
    - output_file_path (str): The path of the output text file.
    """
    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write(lecture_content)

def main(topic, output_file_path):
    """
    Orchestrates the process of generating a lecture based on a topic and writes it to a specified text file.
    """
    lecture_content = generate_lecture_on_topic(topic)
    write_output_to_file(lecture_content, output_file_path)
    print(f"Lecture on '{topic}' written to {output_file_path}")

if __name__ == "__main__":
    topic = "The Impact of Climate Change on Marine Biodiversity"  # Example topic
    output_file_path = "generated_lecture.txt"  # Desired path for the output file
    main(topic, output_file_path)
