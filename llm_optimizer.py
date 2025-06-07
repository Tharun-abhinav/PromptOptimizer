import os
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def rewrite_prompt_with_llm(prompt: str, model="gpt-3.5-turbo", temperature: float = 0.5) -> str:
    """
    Optimizes a given prompt using an LLM to reduce token usage.

    Args:
        prompt (str): The original user prompt.
        model (str): The OpenAI model to use (e.g., "gpt-4").
        temperature (float): Sampling temperature for creativity vs. precision.

    Returns:
        str: The optimized (compressed) prompt.
    """
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a prompt compression assistant. Your goal is to reduce "
                        "the number of tokens in a prompt while preserving its original meaning. "
                        "Use the fewest words possible. Avoid formal phrasing or extra details. "
                        "Return only the compressed version of the prompt."
                    ),
                },
                {"role": "user", "content": f"Original Prompt: '{prompt}'"}
            ],
            temperature=temperature,
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        print(f"[LLM Optimization Error] {e}")
        return prompt  # Return original if optimization fails
