# llm_router.py

from llm_gpt import optimize_with_gpt
from llm_claude import optimize_with_claude
from llm_perplexity import optimize_with_perplexity
from llm_julias import optimize_with_julias

def route_optimizer(prompt: str, model: str) -> str:
    if model in ["gpt-3.5-turbo", "gpt-4"]:
        return optimize_with_gpt(prompt, model)
    elif model.startswith("claude"):
        return optimize_with_claude(prompt, model)
    elif model.startswith("perplexity"):
        return optimize_with_perplexity(prompt)
    elif model == "julias":
        return optimize_with_julias(prompt)
    else:
        return "Unsupported model."
