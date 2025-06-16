import tiktoken
from dotenv import load_dotenv
from text_preprocessor import preprocess_prompt

load_dotenv()

def count_tokens_openai(prompt: str, model: str = "gpt-4") -> int:
    try:
        encoding = tiktoken.encoding_for_model(model)
    except KeyError:
        encoding = tiktoken.get_encoding("cl100k_base")
    return len(encoding.encode(prompt))

def estimate_claude_tokens(prompt: str) -> int:
    return int(len(prompt) / 3.5)  # 1 token ≈ 3.5 characters

def estimate_gemini_tokens(prompt: str) -> int:
    return int(len(prompt.split()) * 1.3)  # 1.3 tokens per word

def count_tokens(prompt: str, model: str) -> int:
    # Preprocess the prompt before tokenization
    preprocessed_prompt = preprocess_prompt(prompt, model)
    
    if model.startswith("gpt"):
        return count_tokens_openai(preprocessed_prompt, model)
    elif "claude" in model:
        return estimate_claude_tokens(preprocessed_prompt)
    elif "gemini" in model:
        return estimate_gemini_tokens(preprocessed_prompt)
    else:
        return len(preprocessed_prompt.split())  # fallback
