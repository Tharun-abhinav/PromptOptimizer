import streamlit as st

from tokenizer import count_tokens
from llm_costs import estimate_cost, get_all_models
import pandas as pd
import matplotlib.pyplot as plt
from text_preprocessor import optimize_prompt

st.set_page_config(page_title="LLM Token Cost Analyzer", page_icon="🧮")

st.title("🧮 LLM Token Cost Analyzer")
st.write("Paste your prompt below to analyze token usage and estimated cost across models.")

prompt = st.text_area("📝 Prompt Input", height=200)

if st.button("Analyze"):
    if prompt.strip() == "":
        st.warning("Please enter a prompt.")
    else:
        results = []
        for model in get_all_models():
            tokens = count_tokens(prompt, model)
            cost = estimate_cost(tokens, model)
            results.append({
                "Model": model,
                "Tokens": tokens,
                "Estimated Cost ($)": cost
            })

        # Show as DataFrame
        df = pd.DataFrame(results)
        st.dataframe(df, use_container_width=True)

        # Bar chart
        fig, ax = plt.subplots()
        ax.bar(df["Model"], df["Estimated Cost ($)"], color="#4c91f0")
        ax.set_ylabel("Estimated Cost ($)")
        ax.set_title("Cost Comparison Across LLMs")
        st.pyplot(fig)

        # Optimization Section moved inside the Analyze button block
        llm_choice = st.selectbox(
            "Select the LLM for Prompt Optimization",
            ["gpt-3.5-turbo", "gpt-4", "claude-3-opus", "claude-3-haiku", "perplexity-mixtral", "julias"]
        )

        st.header("🛠️ Prompt Optimizer")

        optimized_prompt = optimize_prompt(prompt)
        tokens_original = count_tokens(prompt, model="gpt-4")
        tokens_optimized = count_tokens(optimized_prompt, model="gpt-4")

        st.subheader("📉 Token Usage Comparison")

        if tokens_original > 0:
            reduction_percentage = 100 * (1 - tokens_optimized / tokens_original)
            st.markdown(f"""
- 📝 **Original Prompt Tokens:** {tokens_original}  
- ✨ **Optimized Prompt Tokens:** {tokens_optimized}  
- 💡 **Reduction:** {tokens_original - tokens_optimized} tokens (~{reduction_percentage:.2f}%)""")
        else:
            st.markdown(f"""
- 📝 **Original Prompt Tokens:** {tokens_original}  
- ✨ **Optimized Prompt Tokens:** {tokens_optimized}  
- 💡 **Reduction:** N/A (Original prompt has 0 tokens)""")

        st.subheader("🔁 Optimized Prompt")
        st.code(optimized_prompt, language="markdown")
        st.download_button("⬇️ Download Optimized Prompt", optimized_prompt, file_name="optimized_prompt.txt")

        from llm_optimizer import rewrite_prompt_with_llm

        st.subheader("🤖 GPT-3.5 Optimized Prompt")
        if st.button("Generate with GPT-3.5"):
            with st.spinner("Optimizing with LLM..."):
                llm_prompt = rewrite_prompt_with_llm(prompt)
                llm_tokens = count_tokens(llm_prompt, model="gpt-4")
                token_diff = tokens_original - llm_tokens
                st.success("✅ Optimization Complete!")

                st.markdown(f"""
        - 🧠 **LLM Optimized Tokens:** {llm_tokens}  
        - 🧮 **Saved Tokens:** {token_diff}  
        - 🪙 **Estimated Cost Reduction (GPT-4):** ${estimate_cost(token_diff, 'gpt-4')}""")
                st.code(llm_prompt, language="markdown")
                st.download_button("⬇️ Download GPT-Optimized Prompt", llm_prompt, file_name="gpt_optimized_prompt.txt")


