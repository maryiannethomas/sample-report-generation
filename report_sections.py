# ✅ report_generator.py — generates all report sections as a dict
from generator_llm import *

def generate_objectives(context):
    return [
        f"To define and forecast the {context['input_phrase']} market based on components, deployment mode, organisation sixe, application, end-user industry, and region",
        f"To provide detialed information regarding the major facotrs influencing market growth (drivers, restraints, opportunities, and challenges.",
        f"To strategically analyze micro markets concerning indiviual growth trends, fututre prospects, and contributions to the overall {context['input_phrase']} market.",
        f"To analyze opportunities in the market for stakeholders and provide a comprehensive overview of the competitive landscape for market leaders.",
        f"To a forecast the size of the market segments concerning four main regions (along with countries), namely, North America, Europe,Asia Pacific,Latin America, and the Middle East and Africa.",
        f"To access the imapct of ongoing war on the {context['input_phrase']} market in both the short and long terem.",
        f"To strategically analyze the market structure and profile key players along with their core competencies in the global {context['input_phrase']} market ",
        f"To track and analyze competitive developments, such as product launches and approvals, expansions, acquisitions, partnerships, and agreements in the {context['input_phrase']} market."
    ]

def generate_years_of_study(context):
    return [
        f"2022-Historical Year",
        f"2023-Base Year",
        f"2024-e - Estimated Year",
        f"2031-p - Projected Year"
    ]

def generate_currency(context):
    return [
        f"The report utilizes the United States Dollar (USD) as its currency, with market sizes expressed in millions or billions of USD.",
        f"Revenues reported in USD were sourced from the respective annual reports or SEC filings of the companies.",
        f"For companies that reported revenues in currencies other than USD, the average annual exchange rate for the relevant year was applied to convert their figures into USD."
    ]
def generate_limitations(context):
    return[
        f"Some companies within this market are privately held, and their financial data is not publicly accessible.",
        f"Revenue estimates for these companies were gathered from alternative sources, which may lead to discrepancies from actual figures.",
        f"Developments or changes within companies that are not disclosed publicly are excluded from this report.",
        f"For publicly traded companies that did not disclose revenues for specific segments in their annual reports, analysts made assumptions based on various parameters to estimate revenue contributions.",
        f"Given that many key players in this market are privately owned, significant emphasis was placed on market size and growth rate data obtained from primary respondents.",
        f"Market values have been rounded to two decimal places, which may result in minor variations in the figures presented."
    ]
def generate_summary_of_changes(context):
    return[
        f"REFINEMENTS IN THE SEGMENTS OF THE GLOBAL {context['input_phrase']} market",
        f"The current edition of the report includes an analysis of the impact of war on the {context['input_phrase']} market, addressing how geopolitical conflicts have influenced market dynamics and supply chains.",
        f"The market overview section has been expanded to reflect additional insights regarding the implications of ongoing conflicts on market trends and growth projections.",
        f"Country-level data for the Rest of the World (RoW) segment has been further detailed, differentiating between Latin America and the Middle East & Africa to highlight regional variations influenced by war.",
        f"The competitive landscape chapter has been updated to include a market evaluation matrix. This chapter now features a market ranking analysis for 2023, alongside competitive leadership mapping and an assessment of competitive trends and situations shaped by geopolitical tensions.",
        f"Coverage of new players in the transport management system market: The report includes 20 company profiles that provide insights into key players in the transport management system market, highlighting their business overviews, financials, product offerings, and recent developments.",
        f"Updated financial information/product portfolio of players: The latest edition of the report presents updated financial information for each listed company within the transport management system market up to 2023. This information aids in analyzing the current status of the profiled companies regarding their financial strength, profitability, primary revenue-generating regions, business segment focus on the highest revenue-generating areas, and investments in research and development.",
        f"Updated market developments of profiled players: The current edition provides updated developments of the profiled players from January 2022 to December 2024, continuing from the previous version. During this period, product launches and acquisitions have emerged as the primary growth strategies adopted by market players.",
        f"",
        f"LIMITATIONS OF THE CURRENT EDITION",
        f"This edition of the report was published ahead of schedule following the last edition released in December 2023. As a result, certain updates and changes (such as market share analysis) are reflected in the fully updated version of 2024."
    ]
def generate_droq(context):
    return {
        "drivers": generate_drivers(context),
        "restraints": generate_restraints(context),
        "opportunities": generate_opportunities(context),
        "challenges": generate_challenges(context)
    }
def generate_sections(context):
    return {
        "objectives": generate_objectives(context),
        "definition": generate_definition(context),
        "stakeholders": generate_stakeholders(context),
        "executive_summary": generate_executive_summary(context),
        "market_segmentation": generate_market_segmentation(context),
        "key_trends": generate_key_trends(context),
        "investment_landscape": generate_investment_landscape(context),
        "future_outlook": generate_future_outlook(context),
        "swot": generate_swot(context),
        "pestle": generate_pestle(context),
        "porter": generate_porters(context)
    }
def table_of_contents(context):
    return [
        f"1.Introduction", 
        f"1.1.Report Summary",
        f"1.2.Objectives of the Study",
        f"1.3.Market Definition",
        f"1.3.1.Markets Covered", 
        f"1.3.2. Years Considered for the Study", 
        f"1.4.Study Scope",
        f"1.5.Study Limitations", 
        f"1.6.Market Stakeholders",
        f"2.Research Methodology", 
        f"2.1.Secondary Data", 
        f"2.1.1.Key Data from Secondary Sources", 
        f"2.2. Primary Data", 
        f"2.2.1. Key Data from Primary Sources", 
        f"2.3. Demand-Side Analysis", 
        f"2.3.1. Introduction", 
        f"2.3.2.Demand-Side Indicators", 
        f"2.4. Market Size Estimation", 
        f"2.4.1. Bottom-Up Approach", 
        f"2.4.2.Top-Down Approach ",
        f"2.5. Market Breakdown & Data Triangulation", 
        f"2.6. Research Assumptions3.Executive Summary", 
        f"3.1.Porter’s Five Forces analysis", 
        f"3.2. SWOT analysis", 
        f"3.3. PESTLE analysis", 
        f"3.4. Patent analysis.", 
        f"3.4.1. By region (2023–2031)", 
        f"3.4.2.By application4.Market Overview", 
        f"4.1.Market definition and scope ",
        f"4.2. Key findings", 
        f"4.2.1. Total Addressable Market (TAM), 2023-2031",
        f"4.2.2.Pricing Analysis by Segment", 
        f"4.2.3.Factors Impacting Pricing, 2023-2031", 
        f"4.3. Market Segmentation (Historical, Forecast, Marketshare analysis)", 
        f"4.4. By Solutions:", 
        f"4.4.1. Planning and Execution", 
        f"4.4.2.Order Management", 
        f"4.4.3.Audit, Payment, and Claims", 
        f"4.4.4.Analytics and Reporting ",
        f"4.4.5.Routing and Tracking ",
        f"4.5. By Services: ",
        f"4.5.1. Consulting ",
        f"4.5.2.Integration and Implementation", 
        f"4.6. Transportation Management System Dynamics ",
        f"4.6.1. Drivers",
        f"4.6.1.1. Increasing Demand for Real-Time Tracking and Visibility", 
        f"4.6.1.2.Growth in E-commerce and Omni-channel Retailing ",
        f"4.6.1.3.Focus on Cost Reduction and Efficiency ",
        f"4.6.2.Restraints ",
        f"4.6.2.1.High Implementation and Maintenance Costs ",
        f"4.6.2.2.Complexity in Integration with Legacy Systems ",
        f"4.6.3.Opportunities", 
        f"4.6.4.Challenges ",
        f"4.6.5.Macro-Economic Factors ",
        f"4.6.6.Forecast Factors",
        f"5.Pricing Analysis and Value Chain Analysis", 
        f"5.1.1.Pricing Analysis by Segment", 
        f"5.1.2.By Each Region 2023.", 
        f"5.1.3.Factors impacting pricing, 2023-2031.",
        f"6.Transportation Management System, By Region", 
        f"6.1.Market Share Analysis by Region, 2023-2031", 
        f"6.2. Historical and Forecast Analysis by Region 2020-2031", 
        f"6.3. Market Share Analysis by Segments, 2023-2031", 
        f"6.4. Key Takeaway", 
        f"6.5. North America Market. ",
        f"6.5.1. US ",
        f"6.5.2. Canada ",
        f"6.6. Europe ",
        f"6.6.1 UK ",
        f"6.6.2. Germany ",
        f"6.6.3. France"
    ]
    