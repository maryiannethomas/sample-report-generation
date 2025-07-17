# ✅ visuals.py — generates all charts using matplotlib
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import textwrap

def create_market_forecast_chart(years, values, title="Market Size Forecast"):
    fig, ax = plt.subplots(figsize=(7, 3))
    ax.plot(years, values, marker='o', color='green', linewidth=2)
    ax.set_title(title)
    ax.set_xlabel("Year")
    ax.set_ylabel("Market Size (in USD Bn)")
    ax.grid(True)
    return fig

def create_cagr_bar_chart(regions, cagr_values):
    fig, ax = plt.subplots(figsize=(7, 3))
    ax.bar(regions, cagr_values, color='skyblue')
    ax.set_title("CAGR by Region (2023–2031)")
    ax.set_ylabel("CAGR (%)")
    return fig

def create_segment_pie_chart(segments, shares):
    fig, ax = plt.subplots(figsize=(6, 3))
    ax.pie(shares, labels=segments, autopct='%1.1f%%', startangle=90)
    ax.set_title("Market Share by Segment")
    ax.axis('equal')
    return fig

def create_strategy_pyramid():
    fig, ax = plt.subplots(figsize=(5, 4))
    levels = ['Vision', 'Strategy', 'Execution']
    values = [1, 2, 3]
    ax.barh(levels, values, color=['#ffc107', '#2196f3', '#4caf50'])
    ax.set_title("Strategy Execution Pyramid")
    ax.set_xlim(0, 4)
    return fig
import matplotlib.pyplot as plt
import matplotlib.patches as patches

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from generator_llm import *  # You need to define these
import textwrap

def wrap_text(text, width=50):
    return "\n".join(textwrap.wrap(text, width))

import matplotlib.pyplot as plt
import matplotlib.patches as patches


import matplotlib.pyplot as plt
import matplotlib.patches as patches

def create_data_sources_visual():
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.axis('off')

    # Section titles and content
    sections = [
        {
            "title": "MARKET SIZE",
            "sources": [
                "Company Financials",
                "Magazines",
                "Journals",
                "Press Releases",
                "Paid Databases",
                "Dynamics Market Insights Data Repository"
            ],
            "icon": "📈"
        },
        {
            "title": "COMPANY REVENUES",
            "sources": [
                "Annual Reports",
                "Company Websites",
                "Public Databases",
                "Dynamics Markets Insights Data Repository"
            ],
            "icon": "💵"
        },
        {
            "title": "QUALITATIVE INFORMATION\n(Market Dynamics and Trends)",
            "sources": [
                "Company Websites",
                "Annual Reports",
                "Press Releases",
                "Dynamics Markets Insights Data Repository"
            ],
            "icon": "💬"
        }
    ]

    # Background and layout
    start_y = 0.8
    section_height = 0.25
    box_padding = 0.02
    text_x_icon = 0.05
    text_x_param = 0.12
    text_x_source = 0.5

    for idx, section in enumerate(sections):
        y = start_y - idx * section_height

        # Draw section background
        bg = patches.FancyBboxPatch(
            (0.03, y - section_height + box_padding),
            0.94, section_height - box_padding * 2,
            boxstyle="round,pad=0.02", fc="#e0f7fa", ec="#80deea", lw=1.5
        )
        ax.add_patch(bg)

        # Divider line (skip for last block)
        if idx < len(sections) - 1:
            ax.plot([0.03, 0.97], [y - section_height, y - section_height], color="#0097a7", linestyle='--', linewidth=1)

        # Icon + Title
        ax.text(text_x_icon, y - 0.07, section["icon"], fontsize=18)
        ax.text(text_x_param, y - 0.07, section["title"], fontsize=12, weight='bold', va='top')

        # Sources List
        bullet_text = "\n".join([f"• {s}" for s in section["sources"]])
        ax.text(text_x_source, y - 0.05, bullet_text, fontsize=10, va='top')

    # Column Headers
    ax.text(0.12, 0.9, "PARAMETER", fontsize=14, weight='bold')
    ax.text(0.5, 0.9, "SOURCE", fontsize=14, weight='bold')

    return fig

    # Show it
    fig = create_data_sources_visual()
    plt.tight_layout()
    plt.tight_layout()
    
    return fig


def create_market_insights_table(context):
    keyword = context['input_phrase']
    
    sections = [
        {
            "type": "GEOGRAPHIC SPLIT",
            "parameter": [
                "Overall market and subsegments in 2023",
                "CAGR of each region in the forecast period (2024–2031)"
            ],
            "key_data": [
                f"{keyword} Market, by region (North America, Europe, Asia Pacific, Latin America, and the Middle East & Africa)"
            ]
        },
        {
            "type": "GLOBAL MARKET SIZE",
            "parameter": [
                "Global market size for 2023",
                "CAGR for the forecast period (2024–2031)"
            ],
            "key_data": [
                f"{keyword} Market",
                f"{keyword} Market, by method, product, technology, application, and end user"
            ]
        },
        {
            "type": "MARKET SPLIT",
            "parameter": [
                f"The {keyword.lower()} market is segmented by component (software, hardware, services), deployment (cloud, on-premises), organization size (SMEs, large enterprises), industry (e-commerce, manufacturing, logistics, healthcare, etc.), transportation mode (road, rail, air, maritime), and region (North America, Europe, Asia-Pacific, Latin America, Middle East & Africa), reflecting diverse applications and growth areas"
            ],
            "key_data": [
                f"{keyword} Market,",
                "By method", "By product", "By technology", "By application", "By end user"
            ]
        }
    ]

    fig, ax = plt.subplots(figsize=(12, 7))
    ax.axis('off')

    # Headers
    ax.text(0.05, 0.95, "TYPE", fontsize=14, weight='bold')
    ax.text(0.35, 0.95, "PARAMETER", fontsize=14, weight='bold')
    ax.text(0.68, 0.95, "KEY DATA", fontsize=14, weight='bold')

    y = 0.88
    for sec in sections:
        # Background block
        ax.add_patch(patches.FancyBboxPatch((0.03, y - 0.22), 0.94, 0.20, boxstyle="round,pad=0.02", fc="#f1f8e9", ec="#c5e1a5"))

        # Type
        ax.text(0.05, y, sec["type"], fontsize=11, weight='bold', va='top')

        # Parameter
        param_text = "\n".join(textwrap.wrap("\n".join(sec["parameter"]), 60))
        ax.text(0.35, y, param_text, fontsize=10, va='top')

        # Key Data
        key_text = "\n".join(textwrap.wrap("\n".join(sec["key_data"]), 50))
        ax.text(0.68, y, key_text, fontsize=10, va='top')

        y -= 0.26  # space between sections

    return fig
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch
from generator_llm import generate_primary_sources, generate_secondary_sources, generate_information_sourced
import textwrap

def wrap(text, width=45):
    return "\n".join(textwrap.wrap(text, width))

def create_data_triangulation_chart(context):
    # GPT content
    demand_side = generate_primary_sources(context, side="demand", limit=7)
    supply_side = generate_primary_sources(context, side="supply", limit=7)
    secondary = generate_secondary_sources(context, limit=6)
    info_sourced = generate_information_sourced(context, limit=6)

    fig, ax = plt.subplots(figsize=(14, 9))
    ax.axis('off')

    # --- Primary Sources (Left Side)
    ax.text(0.05, 0.92, "PRIMARY SOURCES", fontsize=13, weight='bold', color="#e91e63")
    ax.text(0.05, 0.88, "DEMAND SIDE\nInterviews With:", fontsize=11, weight='bold')
    ax.text(0.05, 0.82, wrap("\n".join([f"• {line}" for line in demand_side])), fontsize=10)

    ax.text(0.05, 0.67, "SUPPLY SIDE\nInterviews With:", fontsize=11, weight='bold')
    ax.text(0.05, 0.61, wrap("\n".join([f"• {line}" for line in supply_side])), fontsize=10)

    # --- Triangle Center
    triangle = plt.Polygon([[0.45, 0.5], [0.63, 0.8], [0.80, 0.5]], color='lightgray', ec="black")
    ax.add_patch(triangle)
    ax.text(0.61, 0.61, "DATA\nTRIANGULATION", fontsize=10, weight='bold', ha='center')

    ax.text(0.46, 0.48, "PRIMARY\nSOURCES", fontsize=9, ha='center', color='#e91e63', weight='bold')
    ax.text(0.80, 0.48, "SECONDARY\nSOURCES", fontsize=9, ha='center', color='navy', weight='bold')

    # --- Secondary Sources (Right Side)
    ax.text(0.83, 0.92, "SECONDARY SOURCES", fontsize=13, weight='bold', color='navy')
    ax.text(0.83, 0.88, wrap("\n".join([f"• {line}" for line in secondary])), fontsize=10)

    # --- Information Sourced (Bottom)
    ax.add_patch(FancyBboxPatch((0.2, 0.30), 0.6, 0.08, boxstyle="round,pad=0.02", fc="#03a9f4", ec="none"))
    ax.text(0.5, 0.33, "INFORMATION SOURCED", fontsize=12, weight='bold', color='white', ha='center')

    cols = info_sourced[:6]
    positions = [(0.2 + i * 0.13, 0.25) for i in range(len(cols))]
    for (x, y), label in zip(positions, cols):
        ax.add_patch(FancyBboxPatch((x, y), 0.12, 0.04, boxstyle="round,pad=0.02", fc="#f8bbd0"))
        ax.text(x + 0.06, y + 0.01, wrap(label), fontsize=8, ha='center')

    return fig
