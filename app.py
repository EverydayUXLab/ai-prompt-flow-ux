import streamlit as st

st.set_page_config(
    page_title="AI Prompt Flow UX Review",
    layout="wide"
)

st.sidebar.title("Audit Sections")
section = st.sidebar.radio(
    "",
    [
        "Overview",
        "Prompt Flow Reviewed",
        "UX Issues Identified",
        "System Feedback & Trust",
        "Outcomes & Recommendations"
    ]
)

st.title("AI Prompt Flow & Response UX Review")
st.caption("AI Product · UX & Performance Audit (Anonymized)")

st.markdown("---")

if section == "Overview":
    st.header("Audit Context")

    st.write(
        """
        This UX audit reviews an AI-driven product where users experienced confusion,
        low trust, and inconsistent outcomes despite strong underlying model performance.

        The product relied on multi-step prompt interactions and asynchronous responses,
        but provided limited guidance and feedback during execution.
        """
    )

    st.info(
        "Focus: prompt clarity, response framing, system feedback, and trust — not model tuning."
    )

elif section == "Prompt Flow Reviewed":
    st.header("Prompt Flow Reviewed")

    st.markdown(
        """
        **Key interaction stages:**
        - Initial user prompt entry
        - System interpretation and clarification steps
        - AI response generation
        - Retry and fallback handling
        """
    )

    st.warning(
        """
        Users often lacked a clear mental model of what the system was doing
        between prompt submission and response delivery.
        """
    )

elif section == "UX Issues Identified":
    st.header("UX Issues Identified")

    st.subheader("Prompt ambiguity")
    st.write(
        """
        - Prompts accepted vague or underspecified inputs
        - No guidance on effective prompt structure
        """
    )

    st.subheader("Response clarity")
    st.write(
        """
        - Responses mixed confidence levels
        - Important caveats were buried or missing
        """
    )

    st.subheader("Failure handling")
    st.write(
        """
        - Retries felt arbitrary
        - Errors lacked actionable guidance
        """
    )

elif section == "System Feedback & Trust":
    st.header("System Feedback & Trust")

    st.markdown(
        """
        **Observed issues:**
        - No progress indicators during generation
        - Silent retries created uncertainty
        - System limitations were not communicated upfront
        """
    )

    st.info(
        "Lack of feedback significantly reduced user trust, even when responses were correct."
    )

elif section == "Outcomes & Recommendations":
    st.header("Outcomes & Value")

    st.markdown(
        """
        **Impact of UX-level recommendations:**
        - Clearer user expectations during prompt execution
        - Improved trust in AI-generated responses
        - Reduced confusion without changing the underlying model
        """
    )

    st.success(
        "All recommendations were UX-level and model-agnostic."
    )
