
from __future__ import annotations

import json
from datetime import datetime

import streamlit as st
import streamlit.components.v1 as components

from buildbetter_logic import (
    ACTIONS,
    AUDIENCES,
    PAINS,
    POLISH_LEVELS,
    PURPOSES,
    best_ai_hint,
    build_prompt,
    clean,
    explain_match,
    infer_deliverable,
)

st.set_page_config(
    page_title="BuildBetter",
    page_icon="BB",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
    :root {
        --bg: #101010;
        --panel: #161616;
        --panel-2: #1b1b1b;
        --line: #2a2a2a;
        --line-soft: #222222;
        --text: #f3f3f1;
        --muted: #b2b2ad;
        --soft: #8c8c87;
        --accent: #ece8df;
        --accent-text: #111111;
        --success: #9fd6a1;
    }

    .stApp {
        background:
            radial-gradient(circle at top right, rgba(255,255,255,0.035), transparent 22%),
            linear-gradient(180deg, #0d0d0d 0%, #111111 100%);
        color: var(--text);
    }

    .block-container {
        max-width: 1180px;
        padding-top: 32px;
        padding-bottom: 44px;
    }

    h1, h2, h3, h4, h5, h6, p, div, span, label {
        color: var(--text);
    }

    .hero {
        border: 1px solid var(--line);
        background: linear-gradient(180deg, rgba(255,255,255,0.028), rgba(255,255,255,0.012));
        border-radius: 20px;
        padding: 28px 30px;
        margin-bottom: 18px;
        box-shadow: 0 20px 60px rgba(0,0,0,0.28);
    }

    .eyebrow {
        color: var(--muted);
        font-size: 12px;
        font-weight: 700;
        letter-spacing: 0.14em;
        text-transform: uppercase;
        margin-bottom: 10px;
    }

    .hero-title {
        font-size: 38px;
        line-height: 1.04;
        font-weight: 700;
        letter-spacing: -0.03em;
        margin-bottom: 10px;
        max-width: 780px;
    }

    .hero-sub {
        color: var(--muted);
        font-size: 15px;
        line-height: 1.55;
        max-width: 840px;
        margin-bottom: 18px;
    }

    .hero-grid {
        display: grid;
        grid-template-columns: repeat(3, minmax(0, 1fr));
        gap: 12px;
        margin-top: 10px;
    }

    .hero-card {
        border: 1px solid var(--line-soft);
        background: rgba(255,255,255,0.018);
        border-radius: 14px;
        padding: 14px 14px 13px 14px;
    }

    .hero-card strong {
        display: block;
        font-size: 14px;
        font-weight: 700;
        margin-bottom: 4px;
    }

    .hero-card span {
        color: var(--muted);
        font-size: 13px;
        line-height: 1.45;
    }

    .panel {
        border: 1px solid var(--line);
        background: linear-gradient(180deg, rgba(255,255,255,0.022), rgba(255,255,255,0.01));
        border-radius: 18px;
        padding: 20px 20px 14px 20px;
        box-shadow: 0 12px 32px rgba(0,0,0,0.18);
        margin-bottom: 18px;
    }

    .panel-title {
        font-size: 18px;
        font-weight: 700;
        letter-spacing: -0.02em;
        margin-bottom: 4px;
    }

    .panel-sub {
        color: var(--muted);
        font-size: 14px;
        line-height: 1.5;
        margin-bottom: 14px;
    }

    .info-card {
        border: 1px solid var(--line-soft);
        background: rgba(255,255,255,0.02);
        border-radius: 14px;
        padding: 14px 14px 12px 14px;
        margin-bottom: 12px;
    }

    .info-label {
        font-size: 11px;
        font-weight: 700;
        color: var(--soft);
        text-transform: uppercase;
        letter-spacing: 0.12em;
        margin-bottom: 6px;
    }

    .info-copy {
        color: var(--muted);
        font-size: 14px;
        line-height: 1.5;
    }

    .small-kicker {
        color: var(--soft);
        font-size: 12px;
        margin-top: 4px;
        margin-bottom: 12px;
    }

    label, .stSelectbox label, .stTextInput label, .stTextArea label {
        font-weight: 600 !important;
        letter-spacing: -0.01em;
    }

    .stTextInput input,
    .stTextArea textarea {
        background: rgba(255,255,255,0.02) !important;
        color: var(--text) !important;
        border: 1px solid var(--line) !important;
        border-radius: 12px !important;
        padding: 12px 14px !important;
        box-shadow: none !important;
    }

    .stTextInput input:focus,
    .stTextArea textarea:focus {
        border: 1px solid #4f4f4f !important;
        box-shadow: none !important;
    }

    div[data-baseweb="select"] > div {
        background: rgba(255,255,255,0.02) !important;
        border: 1px solid var(--line) !important;
        border-radius: 12px !important;
        min-height: 46px !important;
    }

    .stButton > button, .stDownloadButton > button {
        border-radius: 12px !important;
        min-height: 44px !important;
        font-weight: 700 !important;
        letter-spacing: -0.01em !important;
        border: 1px solid var(--line) !important;
    }

    .stButton > button[kind="primary"] {
        background: var(--accent) !important;
        color: var(--accent-text) !important;
        border: none !important;
    }

    .stDownloadButton > button {
        background: rgba(255,255,255,0.04) !important;
        color: var(--text) !important;
    }

    [data-testid="stExpander"] {
        border: 1px solid var(--line);
        border-radius: 14px;
        background: rgba(255,255,255,0.015);
    }

    @media (max-width: 900px) {
        .hero-title { font-size: 30px; }
        .hero-grid { grid-template-columns: 1fr; }
    }
    </style>
    """,
    unsafe_allow_html=True,
)


def copy_button(text: str) -> None:
    safe_text = json.dumps(text)
    components.html(
        f"""
        <div style="margin-top: 6px; margin-bottom: 10px;">
            <button
                onclick='navigator.clipboard.writeText({safe_text}).then(() => {{
                    const el = document.getElementById("copy_status");
                    el.innerText = "Copied to clipboard.";
                    setTimeout(() => el.innerText = "", 1800);
                }})'
                style="
                    background: #ece8df;
                    color: #111111;
                    border: none;
                    border-radius: 12px;
                    padding: 11px 16px;
                    cursor: pointer;
                    font-size: 15px;
                    font-weight: 700;
                    letter-spacing: -0.01em;
                "
            >
                Copy Prompt
            </button>
            <div id="copy_status" style="margin-top:8px;color:#9fd6a1;font-weight:700;font-size:14px;"></div>
        </div>
        """,
        height=76,
    )


st.markdown(
    """
    <div class="hero">
        <div class="eyebrow">BuildBetter • AI Work Translator</div>
        <div class="hero-title">Turn messy team requests into usable AI instructions.</div>
        <div class="hero-sub">
            Built for detail-oriented e-commerce teams that know what needs to get done but do not want to fight with prompt language.
            This tool translates rough business intent into the right request shape so the output is cleaner, faster, and more usable.
        </div>
        <div class="hero-grid">
            <div class="hero-card">
                <strong>Less explaining</strong>
                <span>Start in plain English. The app handles the translation into something an AI can actually use.</span>
            </div>
            <div class="hero-card">
                <strong>Better fit</strong>
                <span>It infers whether the work looks like a plan, reply, SOP, brief, analysis, or customer-facing copy.</span>
            </div>
            <div class="hero-card">
                <strong>Higher trust</strong>
                <span>Clean structure, consistent spacing, and restrained UI so the tool does not undermine the logic.</span>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

left, right = st.columns([1.1, 0.9], gap="large")

with left:
    st.markdown('<div class="panel">', unsafe_allow_html=True)
    st.markdown('<div class="panel-title">Work Intake</div>', unsafe_allow_html=True)
    st.markdown('<div class="panel-sub">Answer in plain English. The app will infer the likely deliverable and build the right AI request.</div>', unsafe_allow_html=True)

    with st.form("buildbetter_form", clear_on_submit=False):
        purpose = st.selectbox("1) What are you trying to get done?", PURPOSES)

        if purpose == "Other":
            purpose_other = st.text_input(
                "Describe what you are trying to get done",
                placeholder="Example: fix store handoff confusion, prepare an investor update, create a better vendor process..."
            )
        else:
            purpose_other = ""

        action = st.selectbox("2) What do you want the AI to do for you?", ACTIONS)

        pain = st.selectbox("3) What is the hardest part right now?", PAINS)
        if pain == "Other":
            pain_other = st.text_input(
                "Describe the hardest part",
                placeholder="Example: everyone is missing details, I need something handoff-ready, I do not know where to start..."
            )
        else:
            pain_other = ""

        goal = st.text_area(
            "4) Describe the work in plain English",
            placeholder="Example: We need a cleaner way to explain our new appointment and styling process without repeating ourselves all day.",
            height=150,
        )

        audience_choice = st.selectbox("5) Who is this for?", AUDIENCES)
        if audience_choice == "Other":
            audience = st.text_input(
                "Describe the audience",
                placeholder="Example: bridal customers, store staff, leadership, paid social traffic..."
            )
        else:
            audience = audience_choice

        details = st.text_area(
            "6) Context, constraints, or must-include details",
            placeholder="deadline, tone, platform, pricing context, brand style, audience concerns, anything that materially matters...",
            height=130,
        )

        polish = st.selectbox("7) How polished does this need to be?", POLISH_LEVELS)

        submitted = st.form_submit_button("Generate the right AI request", type="primary")

    st.markdown('</div>', unsafe_allow_html=True)

with right:
    st.markdown('<div class="panel">', unsafe_allow_html=True)
    st.markdown('<div class="panel-title">What this tool is doing</div>', unsafe_allow_html=True)
    st.markdown('<div class="panel-sub">The goal is not a stronger generic prompt. The goal is the correct prompt type for the work the answers actually represent.</div>', unsafe_allow_html=True)

    st.markdown(
        """
        <div class="info-card">
            <div class="info-label">Example</div>
            <div class="info-copy">
                “We need a better way to explain our return or styling process and I’m tired of repeating it.”
                <br><br>
                The tool can infer: explain something clearly → write it → professional first draft → likely output: FAQ or training guide.
            </div>
        </div>
        <div class="info-card">
            <div class="info-label">Why this matters</div>
            <div class="info-copy">
                Most teams do not fail because they lack ideas. They fail because they cannot translate messy requests into a useful first pass fast enough.
            </div>
        </div>
        <div class="info-card">
            <div class="info-label">Standard</div>
            <div class="info-copy">
                This UI is intentionally restrained. The small details should feel controlled, not accidental.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown('</div>', unsafe_allow_html=True)

if submitted:
    resolved_purpose = purpose_other.strip() if purpose == "Other" and purpose_other.strip() else purpose
    resolved_pain = pain_other.strip() if pain == "Other" and pain_other.strip() else pain

    if not goal.strip():
        st.error("Describe the actual work in plain English.")
    else:
        normalized_purpose = purpose if purpose in PURPOSES else "Other"
        deliverable = infer_deliverable(normalized_purpose, action, resolved_pain)

        data = {
            "timestamp": datetime.now().isoformat(),
            "purpose": resolved_purpose,
            "action": action,
            "pain": resolved_pain,
            "goal": clean(goal),
            "audience": clean(audience),
            "details": clean(details, "None provided"),
            "polish": polish,
            "deliverable": deliverable,
        }

        reasoning_summary = explain_match(normalized_purpose, action, resolved_pain, deliverable)
        ai_hint = best_ai_hint(deliverable)
        prompt = build_prompt(data)

        data["reasoning_summary"] = reasoning_summary
        data["best_ai_hint"] = ai_hint
        data["generated_prompt"] = prompt

        st.markdown('<div class="panel">', unsafe_allow_html=True)
        st.markdown('<div class="panel-title">Recommended Output</div>', unsafe_allow_html=True)
        st.markdown('<div class="panel-sub">The app picks the most likely deliverable shape based on the answers above.</div>', unsafe_allow_html=True)

        c1, c2 = st.columns(2, gap="large")
        with c1:
            st.markdown(
                f"""
                <div class="info-card">
                    <div class="info-label">Best-fit deliverable</div>
                    <div style="font-size: 26px; font-weight: 700; margin-bottom: 8px;">{deliverable}</div>
                    <div class="info-copy">{reasoning_summary}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
        with c2:
            st.markdown(
                f"""
                <div class="info-card">
                    <div class="info-label">Best AI to try first</div>
                    <div style="font-size: 26px; font-weight: 700; margin-bottom: 8px;">{ai_hint}</div>
                    <div class="info-copy">The generated request below is formatted to work cleanly in mainstream models.</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="panel">', unsafe_allow_html=True)
        st.markdown('<div class="panel-title">Ready-to-Copy Prompt</div>', unsafe_allow_html=True)
        st.markdown('<div class="small-kicker">Copy it directly into ChatGPT, Claude, Grok, or a similar tool.</div>', unsafe_allow_html=True)
        st.text_area("Generated Prompt", value=prompt, height=420)
        copy_button(prompt)

        col1, col2 = st.columns(2)
        with col1:
            st.download_button(
                label="Download TXT",
                data=prompt,
                file_name="buildbetter_prompt.txt",
                mime="text/plain",
                use_container_width=True,
            )
        with col2:
            st.download_button(
                label="Download JSON",
                data=json.dumps(data, indent=2),
                file_name="buildbetter_prompt.json",
                mime="application/json",
                use_container_width=True,
            )
        st.markdown('</div>', unsafe_allow_html=True)

        with st.expander("Show captured inputs"):
            st.json(data)

else:
    st.markdown('<div class="panel">', unsafe_allow_html=True)
    st.markdown('<div class="panel-title">What this delivers</div>', unsafe_allow_html=True)
    st.markdown(
        """
        - Translates messy business work into the right AI request  
        - Infers the likely deliverable instead of forcing users to know prompt language  
        - Explains why it chose that format  
        - Produces a copy-ready prompt for ChatGPT, Claude, Grok, or similar tools
        """
    )
    st.markdown('</div>', unsafe_allow_html=True)

st.caption("Run locally or deploy on Streamlit Community Cloud or any internal host.")
