from google import genai
import sys

client = genai.Client()

# Define a function that takes a code diff as input


def review_code(diff_text):

    # Write a multi-line f-string prompt that includes {diff_text}
    # Tell Gemini to act as a code reviewer and focus on security, bugs, performance
    prompt = f""" Gemini, play the role of a code reviewer for {diff_text}.
    Review the code differences with a focus on security, bugs and performance.
    Return the review in a structured format with the following sections:
    - Summary: A brief summary of the changes
    - Security: A list of security issues and descriptions found in the code
    - Bugs: A list of bugs found in the code
    - Performance: A list of performance issues found in the code
    - Score: A score out of 100 for the code review
    - Fix: One suggested fix for each issue found in the code

    If the code is good, return a score of 100 or say its good.
    """

    # Send the prompt to the model and get a response
    response = client.models.generate_content(
        model="gemini-2.5-flash", contents=prompt
    )

    # Return just the text from the response
    return response.text


if __name__ == "__main__":
    if len(sys.argv) > 1:
        diff_file = sys.argv[1]
        with open(diff_file, "r") as f:
            diff_content = f.read()
    else:
        diff_content = sys.stdin.read()

    review = review_code(diff_content)
    print(review)
