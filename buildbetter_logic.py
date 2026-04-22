
from __future__ import annotations

from typing import Dict

PURPOSES = [
    "Sell or market something",
    "Explain something clearly",
    "Create something from scratch",
    "Improve something that already exists",
    "Organize a process or workflow",
    "Respond to a customer, teammate, or lead",
    "Analyze a problem or opportunity",
    "Launch something",
    "Other",
]

ACTIONS = [
    "Write it",
    "Plan it",
    "Analyze it",
    "Improve it",
    "Organize it",
    "Summarize it",
    "Brainstorm it",
    "Recommend the best approach",
]

PAINS = [
    "I do not know what to ask AI for",
    "I need a professional first draft",
    "I need this faster",
    "I need this structured clearly",
    "I need this to sound better",
    "I need something I can hand off to someone else",
    "I need ideas and execution",
    "I am overwhelmed and need a starting point",
    "Other",
]

AUDIENCES = [
    "Customers",
    "Internal team",
    "Leadership",
    "Prospects / leads",
    "Vendors / partners",
    "Mixed audience",
    "Other",
]

POLISH_LEVELS = [
    "Fast draft",
    "Professional",
    "Executive-ready",
    "Customer-facing polished",
]

DELIVERABLE_RULES = {
    "Sell or market something": {
        "Write it": "Landing page copy",
        "Plan it": "Campaign plan",
        "Analyze it": "Offer strategy",
        "Improve it": "Conversion audit",
        "Organize it": "Creative brief",
        "Summarize it": "Brand summary",
        "Brainstorm it": "Campaign concepts",
        "Recommend the best approach": "Offer strategy",
    },
    "Explain something clearly": {
        "Write it": "FAQ",
        "Plan it": "Training guide",
        "Analyze it": "Executive summary",
        "Improve it": "Rewrite",
        "Organize it": "Training guide",
        "Summarize it": "Executive summary",
        "Brainstorm it": "Explanation angles",
        "Recommend the best approach": "Training guide",
    },
    "Create something from scratch": {
        "Write it": "Proposal",
        "Plan it": "Plan",
        "Analyze it": "Strategy document",
        "Improve it": "Strategy document",
        "Organize it": "Checklist",
        "Summarize it": "Concept summary",
        "Brainstorm it": "Concept directions",
        "Recommend the best approach": "Plan",
    },
    "Improve something that already exists": {
        "Write it": "Rewrite",
        "Plan it": "Improvement plan",
        "Analyze it": "Gap analysis",
        "Improve it": "Improvement plan",
        "Organize it": "Optimization recommendations",
        "Summarize it": "Audit summary",
        "Brainstorm it": "Improvement ideas",
        "Recommend the best approach": "Improvement plan",
    },
    "Organize a process or workflow": {
        "Write it": "SOP",
        "Plan it": "Workflow plan",
        "Analyze it": "Role breakdown",
        "Improve it": "Workflow plan",
        "Organize it": "SOP",
        "Summarize it": "Operating guide",
        "Brainstorm it": "Workflow options",
        "Recommend the best approach": "SOP",
    },
    "Respond to a customer, teammate, or lead": {
        "Write it": "Email reply",
        "Plan it": "Follow-up sequence",
        "Analyze it": "Objection handling guide",
        "Improve it": "Customer response",
        "Organize it": "Support playbook",
        "Summarize it": "Reply summary",
        "Brainstorm it": "Response options",
        "Recommend the best approach": "Customer response",
    },
    "Analyze a problem or opportunity": {
        "Write it": "Recommendation memo",
        "Plan it": "Decision framework",
        "Analyze it": "Analysis memo",
        "Improve it": "Recommendation memo",
        "Organize it": "Decision framework",
        "Summarize it": "Executive summary",
        "Brainstorm it": "Opportunity angles",
        "Recommend the best approach": "Recommendation memo",
    },
    "Launch something": {
        "Write it": "Launch brief",
        "Plan it": "Launch plan",
        "Analyze it": "Go-to-market outline",
        "Improve it": "Launch plan",
        "Organize it": "Readiness checklist",
        "Summarize it": "Launch brief",
        "Brainstorm it": "Launch concepts",
        "Recommend the best approach": "Launch plan",
    },
    "Other": {},
}

ROLE_MAP = {
    "Sell or market something": "a senior e-commerce and marketing strategist for a busy retail team",
    "Explain something clearly": "a senior business communicator who turns messy information into clear usable output",
    "Create something from scratch": "a senior strategist who turns vague business needs into execution-ready work",
    "Improve something that already exists": "a senior optimization strategist focused on clarity, conversion, and usability",
    "Organize a process or workflow": "a senior operations strategist who builds clean systems, SOPs, and handoff-ready processes",
    "Respond to a customer, teammate, or lead": "a senior communications strategist skilled in polished, context-aware response writing",
    "Analyze a problem or opportunity": "a senior business analyst and strategic operator",
    "Launch something": "a senior launch strategist who aligns planning, messaging, and execution",
    "Other": "a highly capable, practical business expert",
}

AI_HINTS = {
    "Landing page copy": "Use ChatGPT or Claude.",
    "Campaign plan": "Use ChatGPT or Claude.",
    "Offer strategy": "Use Claude or ChatGPT.",
    "Conversion audit": "Use Claude or ChatGPT.",
    "Creative brief": "Use Claude or ChatGPT.",
    "Brand summary": "Use Claude or ChatGPT.",
    "Campaign concepts": "Use ChatGPT or Claude.",
    "FAQ": "Use ChatGPT or Claude.",
    "Training guide": "Use Claude or ChatGPT.",
    "Executive summary": "Use Claude or ChatGPT.",
    "Rewrite": "Use ChatGPT or Claude.",
    "Explanation angles": "Use ChatGPT or Claude.",
    "Proposal": "Use Claude or ChatGPT.",
    "Plan": "Use Claude or ChatGPT.",
    "Strategy document": "Use Claude or ChatGPT.",
    "Checklist": "Use ChatGPT.",
    "Concept summary": "Use Claude or ChatGPT.",
    "Concept directions": "Use ChatGPT or Claude.",
    "Improvement plan": "Use Claude or ChatGPT.",
    "Gap analysis": "Use Claude or ChatGPT.",
    "Optimization recommendations": "Use Claude or ChatGPT.",
    "Audit summary": "Use Claude or ChatGPT.",
    "Improvement ideas": "Use ChatGPT or Claude.",
    "SOP": "Use Claude or ChatGPT.",
    "Workflow plan": "Use Claude or ChatGPT.",
    "Role breakdown": "Use Claude or ChatGPT.",
    "Operating guide": "Use Claude or ChatGPT.",
    "Workflow options": "Use ChatGPT or Claude.",
    "Email reply": "Use ChatGPT or Claude.",
    "Follow-up sequence": "Use ChatGPT or Claude.",
    "Objection handling guide": "Use Claude or ChatGPT.",
    "Customer response": "Use ChatGPT or Claude.",
    "Support playbook": "Use Claude or ChatGPT.",
    "Reply summary": "Use ChatGPT or Claude.",
    "Response options": "Use ChatGPT or Claude.",
    "Recommendation memo": "Use Claude or ChatGPT.",
    "Decision framework": "Use Claude or ChatGPT.",
    "Analysis memo": "Use Claude or ChatGPT.",
    "Opportunity angles": "Use ChatGPT or Claude.",
    "Launch brief": "Use Claude or ChatGPT.",
    "Launch plan": "Use Claude or ChatGPT.",
    "Go-to-market outline": "Use Claude or ChatGPT.",
    "Readiness checklist": "Use ChatGPT or Claude.",
    "Launch concepts": "Use ChatGPT or Claude.",
}


def clean(text: str, fallback: str = "Not specified") -> str:
    value = (text or "").strip()
    return value if value else fallback


def infer_deliverable(purpose: str, action: str, pain: str) -> str:
    if purpose == "Other":
        pain_l = pain.lower()
        if "reply" in pain_l or "respond" in pain_l:
            return "Email reply"
        if "hand off" in pain_l or "handoff" in pain_l:
            return "SOP"
        return "Plan"

    mapped = DELIVERABLE_RULES.get(purpose, {}).get(action)
    if mapped:
        return mapped

    if purpose == "Organize a process or workflow" and ("hand off" in pain.lower() or "handoff" in pain.lower()):
        return "SOP"

    return "Plan"


def explain_match(purpose: str, action: str, pain: str, deliverable: str) -> str:
    notes = []

    if purpose == "Sell or market something":
        notes.append("This reads like customer-facing commercial work.")
    elif purpose == "Explain something clearly":
        notes.append("This reads like communication work that needs clarity and structure.")
    elif purpose == "Create something from scratch":
        notes.append("This reads like a vague need that has to become a concrete business asset.")
    elif purpose == "Improve something that already exists":
        notes.append("This reads like weak or unfinished work that needs stronger execution.")
    elif purpose == "Organize a process or workflow":
        notes.append("This reads like internal operations work that needs repeatability.")
    elif purpose == "Respond to a customer, teammate, or lead":
        notes.append("This reads like communication that needs a usable draft, not advice.")
    elif purpose == "Analyze a problem or opportunity":
        notes.append("This reads like a decision problem that needs recommendation and structure.")
    elif purpose == "Launch something":
        notes.append("This reads like cross-functional execution work with sequencing and coordination.")
    else:
        notes.append("This needs a structured deliverable instead of a generic answer.")

    if action == "Write it":
        notes.append("The user wants AI to generate the actual content.")
    elif action == "Plan it":
        notes.append("The user needs steps, structure, and sequence.")
    elif action == "Recommend the best approach":
        notes.append("The user wants judgment, not just formatting.")

    pain_l = pain.lower()
    if "professional" in pain_l:
        notes.append("The result needs to be polished enough to use with minimal cleanup.")
    if "faster" in pain_l or "overwhelmed" in pain_l:
        notes.append("Speed matters, so the output should be immediately usable.")
    if "hand off" in pain_l or "handoff" in pain_l:
        notes.append("The output should be easy to pass to someone else.")

    notes.append(f"Best-fit deliverable: {deliverable}.")
    return " ".join(notes)


def best_ai_hint(deliverable: str) -> str:
    return AI_HINTS.get(deliverable, "Use ChatGPT or Claude.")


def output_structure(deliverable: str) -> str:
    structures = {
        "Landing page copy": """Output structure:
1. Page objective
2. Audience positioning
3. Headline options
4. Subheadline
5. Benefit bullets
6. Section-by-section copy
7. CTA options""",
        "Campaign plan": """Output structure:
1. Objective
2. Target audience
3. Core message
4. Offer or hook
5. Channel strategy
6. Execution plan
7. KPI suggestions""",
        "Offer strategy": """Output structure:
1. Goal
2. Offer options
3. Rationale
4. Risks or tradeoffs
5. Recommendation""",
        "Conversion audit": """Output structure:
1. Friction points
2. Messaging gaps
3. Trust issues
4. Recommended fixes
5. Quick wins
6. Bigger improvements""",
        "Creative brief": """Output structure:
1. Objective
2. Audience
3. Core message
4. Tone and feel
5. Deliverables needed
6. Constraints
7. Success criteria""",
        "FAQ": "Output structure:\nCreate a practical FAQ with concise questions and clear answers.",
        "Training guide": """Output structure:
1. Objective
2. Audience
3. Key concepts
4. Step-by-step guidance
5. Common mistakes
6. Quick reference""",
        "Executive summary": """Output structure:
1. Situation
2. Key point
3. What matters most
4. Recommendation
5. Next step""",
        "Rewrite": "Output structure:\nProvide the improved version first, then brief notes on what changed.",
        "Proposal": """Output structure:
1. Objective
2. Proposed solution
3. Benefits
4. Requirements
5. Timeline or next steps""",
        "Plan": """Output structure:
1. Goal
2. Constraints
3. Recommended approach
4. Steps
5. Risks
6. Next actions""",
        "Strategy document": """Output structure:
1. Objective
2. Context
3. Strategy
4. Actions
5. Risks
6. Measurement""",
        "Checklist": """Output structure:
1. Purpose
2. When to use
3. Checklist items in order
4. Final review items""",
        "SOP": """Output structure:
1. Purpose
2. Scope
3. Roles
4. Required inputs
5. Step-by-step procedure
6. Quality checks
7. Escalation notes""",
        "Workflow plan": """Output structure:
1. Goal
2. Current friction
3. Improved workflow
4. Steps
5. Ownership
6. Risks""",
        "Role breakdown": """Output structure:
1. Roles
2. Responsibilities
3. Decision ownership
4. Handoffs
5. Escalation path""",
        "Operating guide": """Output structure:
1. Objective
2. Rules
3. Process
4. Examples
5. Troubleshooting""",
        "Email reply": """Output structure:
1. Best ready-to-send version
2. Shorter version
3. Brief tone note if needed""",
        "Follow-up sequence": """Output structure:
1. Sequence objective
2. Timing
3. Message-by-message drafts
4. CTA logic""",
        "Customer response": """Output structure:
1. Ready-to-send response
2. Warmer version
3. Firmer version""",
        "Support playbook": """Output structure:
1. Purpose
2. Response principles
3. Standard flow
4. Templates
5. Escalation conditions""",
        "Recommendation memo": """Output structure:
1. Situation
2. Options
3. Recommended path
4. Rationale
5. Next actions""",
        "Decision framework": """Output structure:
1. Decision to make
2. Criteria
3. Options
4. Tradeoffs
5. Recommendation""",
        "Analysis memo": """Output structure:
1. Situation
2. Key findings
3. Analysis
4. Risks or opportunities
5. Recommendation""",
        "Launch brief": """Output structure:
1. Launch summary
2. Audience
3. Offer or message
4. Main actions
5. Success definition""",
        "Launch plan": """Output structure:
1. Objective
2. Launch phases
3. Key tasks
4. Dependencies
5. Risks
6. Success measures""",
        "Go-to-market outline": """Output structure:
1. Audience
2. Positioning
3. Offer
4. Channels
5. Launch actions
6. Metrics""",
        "Readiness checklist": "Output structure:\nCreate a grouped launch checklist with final verification items.",
    }
    return structures.get(
        deliverable,
        "Output structure:\nDeliver a complete, polished, immediately usable result with clear headings."
    )


def build_prompt(data: Dict[str, str]) -> str:
    role = ROLE_MAP.get(data["purpose"], ROLE_MAP["Other"])
    return f"""You are {role} supporting a busy e-commerce and boutique retail team.

Your job is to turn the business need below into the correct final deliverable, not generic advice.

Business need:
- Main goal: {data["goal"]}
- What they are trying to get done: {data["purpose"]}
- What kind of help they want from AI: {data["action"]}
- What is hardest right now: {data["pain"]}
- Who this is for: {data["audience"]}
- Context / details: {data["details"]}
- Desired polish level: {data["polish"]}
- Recommended deliverable type: {data["deliverable"]}

Rules:
- Produce the actual deliverable.
- Write with strong commercial judgment, clarity, and polish.
- Make reasonable assumptions if needed and label them briefly.
- Avoid filler and generic AI language.
- Write in a way that saves time for an overloaded team.
- If critical information is missing, deliver the best possible version first, then list missing inputs briefly at the end.

{output_structure(data["deliverable"])}

Final requirement:
Return something polished enough to use immediately."""
