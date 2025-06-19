import streamlit as st
import google.generativeai as genai  # ✅ Add this to check version

# ✅ Debug: show installed package version
st.write("Google GenerativeAI version:", genai.__version__)

from generative_ai import GenerativeAI

generative_ai = GenerativeAI(api_key=st.secrets["GOOGLE_API_KEY"])


def main():
    st.title("Slang Meaning and Usage Generator")
    slang = st.text_input("Enter a slang term:")
    if st.button("Generate Details"):
        if slang:
            result = generative_ai.get_slang_details(slang)
            if "error" in result:
                st.error(f"Failed to fetch slang details. Error: {result['error']}")
            else:
                st.success(f"Meaning of '{slang}': {result['definition']}")
                st.info(f"Usage in a sentence: {result['usage']}")
        else:
            st.warning("Please enter a slang term.")


if __name__ == "__main__":
    main()
