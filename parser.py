from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = (
    "You are tasked with extracting specific information from the following text content: {dom_content}. "
    "Please follow these instructions carefully: \n\n"
    "1. **Extract Information:** Only extract the information that directly matches the provided description: {parse_description}. "
    "2. **No Extra Content:** Do not include any additional text, comments, or explanations in your response. "
    "3. **Empty Response:** If no information matches the description, return an empty string ('')."
    "4. **Direct Data Only:** Your output should contain only the data that is explicitly requested, with no other text."
)

model = OllamaLLM(model="llama3.2")

def get_llm_result(content, user_prompt):
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model

    parsed_result = []
    splited_content = split_content(content)

    for i, chunk in enumerate(splited_content, start=1):
        result = chain.invoke({"dom_content": chunk, "parse_description": user_prompt})
        print(f"Parsed batch: {i} of {len(content)}")
        parsed_result.append(result)
    return "\n".join(parsed_result)

def split_content(content, max_length=6000):
    return [content[i:i + max_length] for i in range(0, len(content), max_length)]
