
from buildbetter_logic import (
    best_ai_hint,
    build_prompt,
    clean,
    explain_match,
    infer_deliverable,
    output_structure,
)


def test_clean_handles_blank_values():
    assert clean("", "Fallback") == "Fallback"
    assert clean("  hello  ") == "hello"


def test_infer_deliverable_for_marketing_write():
    assert infer_deliverable("Sell or market something", "Write it", "I need this faster") == "Landing page copy"


def test_infer_deliverable_for_workflow_handoff():
    result = infer_deliverable("Organize a process or workflow", "Organize it", "I need something I can hand off to someone else")
    assert result == "SOP"


def test_infer_deliverable_for_other_reply_pattern():
    result = infer_deliverable("Other", "Write it", "Need to respond to someone quickly")
    assert result == "Email reply"


def test_explain_match_mentions_deliverable():
    text = explain_match("Sell or market something", "Write it", "I need a professional first draft", "Landing page copy")
    assert "Best-fit deliverable: Landing page copy." in text


def test_best_ai_hint_has_default():
    assert best_ai_hint("Unknown") == "Use ChatGPT or Claude."


def test_output_structure_contains_launch_phases():
    structure = output_structure("Launch plan")
    assert "Launch phases" in structure


def test_build_prompt_contains_goal_and_deliverable():
    prompt = build_prompt({
        "purpose": "Sell or market something",
        "action": "Write it",
        "pain": "I need this faster",
        "goal": "Increase bookings for styling appointments",
        "audience": "Customers",
        "details": "Focus on clarity and premium service",
        "polish": "Customer-facing polished",
        "deliverable": "Landing page copy",
    })
    assert "Increase bookings for styling appointments" in prompt
    assert "Landing page copy" in prompt
    assert "busy e-commerce and boutique retail team" in prompt
