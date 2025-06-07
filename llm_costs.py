MODEL_PRICING = {
    "gpt-3.5-turbo": {
        "input_cost_per_1k": 0.0015,
        "output_cost_per_1k": 0.002,
    },
    "gpt-4": {
        "input_cost_per_1k": 0.03,
        "output_cost_per_1k": 0.06,
    },
    "claude-3-sonnet": {
        "input_cost_per_1k": 0.003,
        "output_cost_per_1k": 0.015,
    },
    "gemini-pro": {
        "input_cost_per_1k": 0.002,
        "output_cost_per_1k": 0.004,
    }
}

def estimate_cost(token_count, model="gpt-4"):
    if model not in MODEL_PRICING:
        return None

    pricing = MODEL_PRICING[model]
    input_cost = (token_count / 1000) * pricing["input_cost_per_1k"]
    return round(input_cost, 5)

def get_all_models():
    return list(MODEL_PRICING.keys())
