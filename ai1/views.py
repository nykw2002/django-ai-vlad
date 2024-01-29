# from django.shortcuts import render
# import openai
# import json
# from PyPDF2 import PdfReader



# open_ai_key = "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"
# client = openai.OpenAI(api_key=open_ai_key)

# # Create your views here.
# def home(request):
#     client.fine_tuning.jobs.create(
#         training_file="output_jsonl_file.jsonl",
#         model="gpt-3.5-turbo",
#     )
        


#     context = {'data': "test returned data"}
#     return render(request, 'home.html', context)


# def chat_with_openai(client, prompt):
#     response = client.chat.completions.create(
#         model="gpt-3.5-turbo-1106",  
#         messages=[
#             {"role": "system", "content": "You are a helpful assistant."},
#             {"role": "user", "content": prompt}
#         ]
#     )
#     return response.choices[0].message


# def main():
#     api_key = input("Please enter your OpenAI API key: ")
#     if not api_key:
#         raise ValueError("API key not provided.")
    
#     openai.api_key = api_key
#     while True:
#         user_prompt = input("You: ")  # Ask the user for a prompt
#         if user_prompt.lower() == "exit":
#             break  # Exit the loop if the user enters "exit"
#         client = openai.OpenAI(api_key = api_key)
#         response = chat_with_openai(client, user_prompt)
#         print("AI: "+ str(list(response)[0][1]))

# if __name__ == "__main__":
#     main()





# # def extract_text_from_pdf(pdf_path):
# #     with open(pdf_path, 'rb') as file:
# #         reader = PdfFileReader(file)
# #         text = ""
# #         for page in range(reader.numPages):
# #             text += reader.getPage(page).extractText()
# #         return text

# def extract_text_from_pdf(pdf_path):
#     with open(pdf_path, 'rb') as file:
#         reader = PdfReader(file)
#         text = ""
#         for page in reader.pages:
#             text += page.extract_text() + "\n"  # Adding a newline for separation between pages
#         return text

# def format_text_to_jsonl(text, jsonl_file_path):
#     paragraphs = text.split('\n\n')  # Splitting the text into paragraphs or sections

#     with open(jsonl_file_path, 'w') as jsonl_file:
#         for paragraph in paragraphs:
#             if paragraph.strip():  # Ensure the paragraph is not just whitespace
#                 # Each paragraph is a separate JSON object
#                 json_obj = {"content": paragraph.strip()}
#                 jsonl_file.write(json.dumps(json_obj, ensure_ascii=False) + '\n')



# def check_jsonl_file(jsonl_file_path):
#     with open(jsonl_file_path, 'r') as file:
#         line_number = 0
#         for line in file:
#             line_number += 1
#             try:
#                 # Attempt to parse the line as JSON
#                 json.loads(line)
#             except json.JSONDecodeError:
#                 # If an error is raised, the line is not valid JSON
#                 print(f"Invalid JSON on line {line_number}: {line.strip()}")
#                 return False
#     return True

# # Example usage
# # jsonl_file_path = 'C:\Users\nicul\OneDrive\Desktop\django-ai-vlad\output_jsonl_file.jsonl'  # Replace with your JSONL file path
# # if check_jsonl_file(jsonl_file_path):
# #     print("All lines in the JSONL file are valid JSON objects.")
# # else:
# #     print("The JSONL file contains invalid JSON.")


# def home(request):
#     # Path to your JSONL file
#     jsonl_file_path = 'output_jsonl_file.jsonl'  # Update with actual path

#     # Check if the JSONL file is valid before proceeding
#     if check_jsonl_file(jsonl_file_path):
#         client.fine_tuning.jobs.create(
#             training_file=jsonl_file_path,
#             model="gpt-3.5-turbo",
#         )
#         message = "Fine-tuning job created successfully."
#     else:
#         message = "Error: Invalid JSONL file."

#     context = {'data': message}
#     return render(request, 'home.html', context)






# def convert_pdf_to_jsonl(pdf_path, jsonl_file_path):
#     extracted_text = extract_text_from_pdf(pdf_path)
#     format_text_to_jsonl(extracted_text, jsonl_file_path)

# # Example usage
# pdf_path = 'knowledge.pdf'  # Replace with your PDF file path
# jsonl_file_path = 'output_jsonl_file.jsonl'  # Replace with your desired output file path
# convert_pdf_to_jsonl(pdf_path, jsonl_file_path)




# from django.shortcuts import render
# import openai
# import json
# from PyPDF2 import PdfReader
# import os

# # Set your OpenAI API key in an environment variable for security
# openai.api_key = os.getenv('OPENAI_API_KEY')


# open_ai_key = "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"
# client = openai.OpenAI(api_key=open_ai_key)


# def upload_file_to_openai(file_path):
#     try:
#         with open(file_path, 'rb') as f:
#             response = openai.File.create(file=f, purpose='fine-tune')
#             return response.id  # Returns the file ID
#     except Exception as e:
#         return f"Error uploading file to OpenAI: {str(e)}"

# # Define your views here
# def home(request):
#     jsonl_file_path = 'output_jsonl_file.jsonl'  # Update with the actual path

#     if check_jsonl_file(jsonl_file_path):
#         client.fine_tuning.jobs.create(
#          training_file="output_jsonl_file.jsonl",
#          model="gpt-3.5-turbo",
#      )
        
#         message = "Fine-tuning job created successfully."
#     else:
#         message = "Error: Invalid JSONL file."

#     context = {'data': message}
#     return render(request, 'home.html', context)

# def chat_with_openai(prompt):
#     try:
#         response = openai.ChatCompletion.create(
#             model="gpt-3.5-turbo-1106",  
#             messages=[
#                 {"role": "system", "content": "You are a helpful assistant."},
#                 {"role": "user", "content": prompt}
#             ]
#         )
#         return response.choices[0].message
#     except Exception as e:
#         return f"An error occurred: {str(e)}"

# def main():
#     while True:
#         user_prompt = input("You: ")
#         if user_prompt.lower() == "exit":
#             break
#         response = chat_with_openai(user_prompt)
#         print("AI: " + response)

# if __name__ == "__main__":
#     main()


# def extract_text_from_pdf(pdf_path):
#     try:
#         with open(pdf_path, 'rb') as file:
#             reader = PdfReader(file)
#             text = ""
#             for page in reader.pages:
#                 page_text = page.extract_text()
#                 if page_text:  # Check if text was extracted
#                     text += page_text + "\n"  # Adding a newline for separation between pages
#             return text
#     except Exception as e:
#         return f"Error reading PDF file: {str(e)}"

# def format_text_to_jsonl(text, jsonl_file_path):
#     try:
#         paragraphs = text.split('\n\n')  # Splitting the text into paragraphs or sections
#         with open(jsonl_file_path, 'w') as jsonl_file:
#             for paragraph in paragraphs:
#                 if paragraph.strip():  # Ensure the paragraph is not just whitespace
#                     json_obj = {"content": paragraph.strip()}
#                     jsonl_file.write(json.dumps(json_obj, ensure_ascii=False) + '\n')
#     except Exception as e:
#         return f"Error writing to JSONL file: {str(e)}"

# def check_jsonl_file(jsonl_file_path):
#     try:
#         with open(jsonl_file_path, 'r') as file:
#             line_number = 0
#             for line in file:
#                 line_number += 1
#                 json.loads(line)  # Attempt to parse the line as JSON
#         return True
#     except json.JSONDecodeError as e:
#         print(f"Invalid JSON on line {line_number}: {line.strip()} - Error: {str(e)}")
#         return False
#     except FileNotFoundError:
#         print(f"File not found: {jsonl_file_path}")
#         return False
#     except Exception as e:
#         print(f"An error occurred while checking the JSONL file: {str(e)}")
#         return False

# def convert_pdf_to_jsonl(pdf_path, jsonl_file_path):
#     extracted_text = extract_text_from_pdf(pdf_path)
#     if isinstance(extracted_text, str):
#         format_text_to_jsonl(extracted_text, jsonl_file_path)
#     else:
#         print(extracted_text)  # Print error message if PDF extraction fails




# # Example usage for PDF to JSONL conversion
# def example_pdf_to_jsonl_conversion():
#     pdf_path = 'knowledge.pdf'  # Replace with your PDF file path
#     jsonl_file_path = 'output_jsonl_file.jsonl'  # Replace with your desired output file path
#     convert_pdf_to_jsonl(pdf_path, jsonl_file_path)

# # Call this function for testing or put it inside if __name__ == "__main__":
# # example_pdf_to_jsonl_conversion()


from django.shortcuts import render
import openai
import json
from PyPDF2 import PdfReader
import os

# Set your OpenAI API key in an environment variable for security
openai.api_key = os.getenv('OPENAI_API_KEY')


open_ai_key = "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"
client = openai.OpenAI(api_key=open_ai_key)

def chat_view(request):
    if request.method == "POST":
        user_input = request.POST.get("user_input")
        response = chat_with_openai(user_input)
        context = {'response': response, 'user_input': user_input}
        return render(request, 'chat.html', context)
    else:
        return render(request, 'chat.html')



def upload_file_to_openai(file_path):
    try:
        with open(file_path, 'rb') as f:
            response = openai.File.create(file=f, purpose='fine-tune')
            return response.id  # Returns the file ID
    except Exception as e:
        return f"Error uploading file to OpenAI: {str(e)}"


def create_fine_tuning_job(file_id):
    try:
        response = openai.FineTune.create(
            training_file=file_id,
            model="gpt-3.5-turbo",  # Replace with the model you are using
            # Add other parameters as needed
        )
        return response
    except Exception as e:
        print(f"Error in creating fine-tuning job: {e}")
        return None

# if dataset_file_id:
#     fine_tuning_response = create_fine_tuning_job(dataset_file_id)
#     print(fine_tuning_response)



# Define your views here
def home(request):
    jsonl_file_path = 'output_jsonl_file.jsonl'  # Update with the actual path

    # if check_jsonl_file(jsonl_file_path):
    #     client.fine_tuning.jobs.create(
    #      training_file="output_jsonl_file.jsonl",
    #      model="gpt-3.5-turbo",
    #  )
        
    #     message = "Fine-tuning job created successfully."
    # else:
    message = "Error: Invalid JSONL file."

    context = {'data': message}
    return render(request, 'home.html', context)

def chat_with_openai(prompt):
    try:
        response=client.fine_tuning.jobs.create(
          training_file="output_jsonl_file.jsonl",
          model="gpt-3.5-turbo",
        
             messages=[
                 {"role": "system", "content": "You are a helpful assistant."},
                 {"role": "user", "content": prompt}
             ]
        )
        return response.choices[0].message
    except Exception as e:
        return f"An error occurred: {str(e)}"

def main():
    while True:
        user_prompt = input("You: ")
        if user_prompt.lower() == "exit":
            break
        response = chat_with_openai(user_prompt)
        print("AI: " + response)

if __name__ == "__main__":
    main()


def extract_text_from_pdf(pdf_path):
    try:
        with open(pdf_path, 'rb') as file:
            reader = PdfReader(file)
            text = ""
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:  # Check if text was extracted
                    text += page_text + "\n"  # Adding a newline for separation between pages
            return text
    except Exception as e:
        return f"Error reading PDF file: {str(e)}"

def format_text_to_jsonl(text, jsonl_file_path):
    try:
        paragraphs = text.split('\n\n')  # Splitting the text into paragraphs or sections
        with open(jsonl_file_path, 'w') as jsonl_file:
            for paragraph in paragraphs:
                if paragraph.strip():  # Ensure the paragraph is not just whitespace
                    json_obj = {"content": paragraph.strip()}
                    jsonl_file.write(json.dumps(json_obj, ensure_ascii=False) + '\n')
    except Exception as e:
        return f"Error writing to JSONL file: {str(e)}"

def check_jsonl_file(jsonl_file_path):
    try:
        with open(jsonl_file_path, 'r') as file:
            line_number = 0
            for line in file:
                line_number += 1
                json.loads(line)  # Attempt to parse the line as JSON
        return True
    except json.JSONDecodeError as e:
        print(f"Invalid JSON on line {line_number}: {line.strip()} - Error: {str(e)}")
        return False
    except FileNotFoundError:
        print(f"File not found: {jsonl_file_path}")
        return False
    except Exception as e:
        print(f"An error occurred while checking the JSONL file: {str(e)}")
        return False

def convert_pdf_to_jsonl(pdf_path, jsonl_file_path):
    extracted_text = extract_text_from_pdf(pdf_path)
    if isinstance(extracted_text, str):
        format_text_to_jsonl(extracted_text, jsonl_file_path)
    else:
        print(extracted_text)  # Print error message if PDF extraction fails




# Example usage for PDF to JSONL conversion
def example_pdf_to_jsonl_conversion():
    pdf_path = 'knowledge.pdf'  # Replace with your PDF file path
    jsonl_file_path = 'output_jsonl_file.jsonl'  # Replace with your desired output file path
    convert_pdf_to_jsonl(pdf_path, jsonl_file_path)

# Call this function for testing or put it inside if __name__ == "__main__":
# example_pdf_to_jsonl_conversion()
