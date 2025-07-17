import streamlit as st
from generator_llm import *
from report_sections import *
from visuals import *
from export import *



st.set_page_config(
    page_title="Market Report Generator",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar Inputs
st.sidebar.title("🧠 Market Report Generator")
keyword_primary = st.sidebar.text_input("Primary Keyword")
keyword_secondary1 = st.sidebar.text_input("Secondary Keyword 1")
keyword_secondary2 = st.sidebar.text_input("Secondary Keyword 2")
use_llm = st.sidebar.checkbox("Use AI for Full Report", value=True)

# Button to trigger generation
if st.sidebar.button("🔍 Generate Report"):
    context = {
        "input_phrase": f"{keyword_primary} {keyword_secondary1} {keyword_secondary2}".strip()
    }

    st.title(f"📄 Market Report: {context['input_phrase']}")

    st.header("Objectives")
    objectives = generate_objectives(context)
    for obj in objectives:
        st.markdown(f"- {obj}")

    st.header("Definition")
    definition = generate_definition(context)
    st.write(definition)

    st.header("Market Segmentation")
    segmentation = generate_market_segmentation(context)
    st.write(segmentation)

    st.header("Years Considered for the study")
    YOS= generate_years_of_study(context)
    for i in YOS:
        st.markdown(f"-{i}")

    st.header("Currency")
    currency=generate_currency(context)
    for m in currency:
        st.markdown(f"- {m}")


    st.header("Limitations")
    limitations=generate_limitations(context)
    for l in limitations:
        st.markdown(f"- {l}")


    st.header("Stakeholders")
    stakeholders = generate_stakeholders(context)
    st.write(stakeholders)
    st.header("Research Methodology")
    st.header("Research Data")
    st.write("This research study involved the extensive use of both primary and secondary data sources. The research process involved the study of various factors affecting the industry, such as the competitive scenario, historical data, current trends in the market, technological innovation, and market dynamics (such as drivers, restraints, opportunities, and challenges). The following figure shows the market research methodology applied in making this report on the transportation management system market.")
    st.header("Research Design")
    st.write(" Market Share, Competitive Landscape, Company Revenues & R&D Expenses, Geographic Usage Pattern")
    st.write("Influencing Factors (Market Trends and Dynamics)")
    droq= generate_droq(context)
    for d in droq:
        st.markdown(f"- {d}")

    st.write("Forecast")
    st.write("Historical Data of the Market")
    st.write("Impact Analysis of Market Trends")
    st.write("Market Size & Forecast")
    st.write("Arrive at the Market Size, Share and CAGR for the market forecast")

    st.header("Secondary Data")
    st.write("During the secondary research process, information was gathered from a variety of sources, including annual reports, press releases, investor presentations, white papers, reputable publications, articles by recognized authors, high-quality websites, directories, and databases. Secondary research was utilized to identify and compile information crucial for a comprehensive technical, market-oriented, and commercial analysis of the transport management system market. It also provided valuable insights into the leading players, market classification and segmentation in line with industry trends down to the finest details, and significant developments related to market and technology perspectives. Additionally, a database of key industry leaders was created based on the findings from secondary research.")
    st.header("Secondary Sources")
    fig_sources = create_data_sources_visual()
    st.pyplot(fig_sources)

    st.header("Primary Data")
    st.write("In the primary research process, various sources from both the supply and demand sides were interviewed to gather qualitative and quantitative information for this report. Primary sources primarily include industry experts from core and related sectors, as well as preferred suppliers, manufacturers, distributors, technology developers, researchers, and organizations connected to all segments of the transport management system industry’s value chain. In-depth interviews were conducted with various primary respondents, including key industry participants, subject-matter experts (SMEs), C-level executives of leading market players, and industry consultants, among others, to obtain and verify essential qualitative and quantitative insights and assess future prospects. Primary research was carried out to identify segmentation types, industry trends, key players, and critical market dynamics, such as drivers, opportunities, challenges, industry trends, and strategies employed by key players.")

    st.header("Key Data from Primary Sources")
    from visuals import create_market_insights_table

    fig = create_market_insights_table(context)
    st.pyplot(fig)

    st.header("Market Breakdown and Data Triangulation")
    st.write("Following the estimation of the overall market size through the previously described processes, the total market was divided into several segments and subsegments. To complete the overall market engineering process and obtain precise statistics for each segment and subsegment, data triangulation and market breakdown methodologies were utilized where applicable. This data triangulation involved analyzing various factors and trends from both the demand and supply sides. Additionally, the market was validated using both top-down and bottom-up approaches to ensure accuracy and reliability in the findings.")

    st.write("Data Triangulation Methodology- image has not been generated")

    st.header("Assumptions of the Study")

    st.header("Table of Contents")
    toc = table_of_contents(context)
    for j in toc:
        st.markdown(f" {j}")
    st.header("Executive Summary")
    exec_summary = generate_executive_summary(context)
    st.write(exec_summary)

    

    st.header("Key Trends")
    trends = generate_key_trends(context)
    st.write(trends)

    st.header("Investment Landscape")
    investments = generate_investment_landscape(context)
    st.write(investments)

    st.header("Future Outlook")
    outlook = generate_future_outlook(context)
    st.write(outlook)

    st.header("SWOT Analysis")
    swot = generate_swot(context)
    st.write(swot)

    st.header("PESTLE Analysis")
    pestle = generate_pestle(context)
    st.write(pestle)

    st.header("Porter's Five Forces")
    porter = generate_porters(context)
    st.write(porter)

    # Charts
    st.header("Visual Charts")
    fig1 = create_market_forecast_chart(list(range(2023, 2032)), [40, 46, 53, 60, 69, 80, 92, 105, 120], "Market Size")
    fig2 = create_cagr_bar_chart(["NA", "EU", "APAC", "LATAM", "MEA"], [6, 5, 7, 4, 3])
    fig3 = create_segment_pie_chart(["Retail", "Manufacturing", "Healthcare"], [30, 40, 30])
    fig4 = create_strategy_pyramid()
    st.pyplot(fig1)
    st.pyplot(fig2)
    st.pyplot(fig3)
    st.pyplot(fig4)


    import traceback

    if st.button("📄 Generate Report PDF"):
        with st.spinner("Generating PDF..."):
            try:
                pdf_path = generate_pdf_report(context)

                if os.path.exists(pdf_path):
                    with open(pdf_path, "rb") as f:
                        st.download_button(
                            label="📥 Download Report",
                            data=f,
                            file_name="market_report.pdf",
                            mime="application/pdf"
                        )
                    os.remove(pdf_path)
                else:
                    st.error("PDF generation failed. File not found.")

            except Exception as e:
                st.error("An error occurred during PDF generation.")
                st.text(f"{type(e).__name__}: {e}")
                st.text(traceback.format_exc())




else:
    st.write("👈 Enter keywords in the sidebar and click Generate Report to get started.")
