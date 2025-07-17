import requests
import os

api_key = os.getenv("TOGETHER_API_KEY")
TOGETHER_API_URL = "https://api.together.xyz/v1/chat/completions"
TOGETHER_MODEL = "mistralai/Mistral-7B-Instruct-v0.2"

def generate_text(prompt, max_tokens=400, stop="###"):
    headers = {
        "Authorization": f"Bearer {TOGETHER_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": TOGETHER_MODEL,
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        "max_tokens": max_tokens,
        "temperature": 0.7,
        "stop": [stop]
    }

    response = requests.post(TOGETHER_API_URL, headers=headers, json=data)
    response.raise_for_status()

    result = response.json()
    content = result["choices"][0]["message"]["content"].strip()
    return content


# Section generators using clean prompts
def generate_definition(context):
    prompt = f"""Define {context['input_phrase']} in formal business terms. In the same paragraph also include use cases importance/relevance of the {context['input_phrase']} all in 100 words']"""
    return generate_text(prompt)

def generate_market_segmentation(context):
    prompt = f"""Describe the market segmentation for {context['input_phrase']} by: 
    in this section come up with 6 relevant segments for thismarket for instance by solutions, services, industry vertical, one of the segments will be By Region:
     -North America US Canada
     -Euorope Germany, UK, France,Italy,Spain,Rest of Europe
     -Asia Pacific China, Japan, India , Rest of Asia Pacific
     -Latin America
     -Middle East & Africa"""
    return generate_text(prompt)

def generate_stakeholders(context):
    prompt = f"""Identify the main stakeholders in the {context['input_phrase']} industry.
Discuss: consumers, producers, investors, regulators, and tech providers."""
    return generate_text(prompt)

def generate_drivers(context):
    prompt = f"List 5 key drivers for the {context['input_phrase']} market."
    raw = generate_text(prompt)
    return [line.strip("-• ") for line in raw.split("\n") if line.strip()]

def generate_restraints(context):
    prompt = f"List 2 key restraints for the {context['input_phrase']} market."
    raw = generate_text(prompt)
    return [line.strip("-• ") for line in raw.split("\n") if line.strip()]

def generate_opportunities(context):
    prompt = f"List 2 key opportunities for the {context['input_phrase']} market."
    raw = generate_text(prompt)
    return [line.strip("-• ") for line in raw.split("\n") if line.strip()]
def generate_challenges(context):
    prompt = f"List 2 key challenges for the {context['input_phrase']} market."
    raw = generate_text(prompt)
    return [line.strip("-• ") for line in raw.split("\n") if line.strip()]


def extract_segments(segmentation_text):
    import re
    match = re.search(r"\(.*?\)", segmentation_text)
    if match:
        raw = match.group(0).strip("()")
        return [s.strip() for s in raw.split(",")]
    return ["Segment A", "Segment B", "Segment C"]
def generate_primary_sources(context, side="demand", limit=6):
    prompt = f"""
List {limit} people/roles interviewed from the {side} side of the {context['input_phrase']} market.
Avoid repeating. Provide concise job titles only.
"""
    raw = generate_text(prompt)
    return [line.strip("-• ").strip() for line in raw.splitlines() if line.strip()]

def generate_secondary_sources(context, limit=6):
    prompt = f"""
List {limit} secondary sources used for market research in the {context['input_phrase']} domain.
Focus on websites, reports, institutions, or data sources.
"""
    raw = generate_text(prompt)
    return [line.strip("-• ").strip() for line in raw.splitlines() if line.strip()]
def generate_information_sourced(context, limit=6):
    prompt = f"""
List {limit} types of information typically derived during market research in the {context['input_phrase']} industry.
"""
    raw = generate_text(prompt)
    return [line.strip("-• ").strip() for line in raw.splitlines() if line.strip()]

def generate_executive_summary(context):
    prompt = f"""Write an executive summary for a market report on {context['input_phrase']}.
Include:
- Key market trends
- Drivers and challenges
- Future outlook till 2031"""
    return generate_text(prompt)

def generate_swot(context):
    prompt = f"""Create a SWOT analysis for {context['input_phrase']}:
Strengths:
Weaknesses:
Opportunities:
Threats:"""
    return generate_text(prompt)

def generate_pestle(context):
    prompt = f"""Provide a PESTLE analysis for the {context['input_phrase']} market.
Structure by: Political, Economic, Social, Technological, Legal, Environmental."""
    return generate_text(prompt)

def generate_porters(context):
    prompt = f"""Write a Porter's Five Forces analysis of {context['input_phrase']}.
Include:
1. Threat of New Entrants
2. Bargaining Power of Suppliers
3. Bargaining Power of Buyers
4. Threat of Substitutes
5. Competitive Rivalry"""
    return generate_text(prompt)



def generate_key_trends(context):
    prompt = f"""List the key trends shaping the {context['input_phrase']} industry.
Focus on:
- Technology adoption
- Consumer behavior
- Regulatory shifts"""
    return generate_text(prompt)

def generate_investment_landscape(context):
    prompt = f"""Analyze the investment landscape for {context['input_phrase']}:
- Recent funding
- M&A activity
- Investor focus areas"""
    return generate_text(prompt)

def generate_future_outlook(context):
    prompt = f"""Forecast the future of the {context['input_phrase']} market.
Include:
- Projections till 2031
- Innovation pipeline
- Market disruptions"""
    return generate_text(prompt)
