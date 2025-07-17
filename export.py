# ✅ export.py — Final version with full PDF layout using ReportLab
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch, cm
import tempfile
import os

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name='SectionHeading', fontSize=14, leading=16, spaceAfter=10, spaceBefore=20, fontName='Helvetica-Bold'))
styles.add(ParagraphStyle(name='NormalText', fontSize=11, leading=15, spaceAfter=8, fontName='Helvetica'))

def header_footer(canvas, doc):
    canvas.saveState()
    width, height = A4

    # Header
    canvas.setFont('Helvetica-Bold', 10)
    canvas.drawString(2 * cm, height - 1.2 * cm, "TRANSPORTATION MANAGEMENT SYSTEM MARKET REPORT")
    canvas.setFont('Helvetica', 8)
    canvas.drawRightString(width - 2 * cm, height - 1.2 * cm, f"Page {doc.page}")

    # Footer
    canvas.setFont('Helvetica', 8)
    canvas.drawString(2 * cm, 1.5 * cm, "https://www.dynamicmarketinsights.com/")
    canvas.drawRightString(width - 2 * cm, 1.5 * cm, "© DynamicsMarketInsights™")

    canvas.restoreState()

def section(title, body):
    elements = [Paragraph(title, styles['SectionHeading'])]
    if isinstance(body, str):
        elements.append(Paragraph(body, styles['NormalText']))
    elif isinstance(body, list):
        for para in body:
            elements.append(Paragraph(f"• {para}", styles['NormalText']))
    elif isinstance(body, dict):
        for k, v in body.items():
            elements.append(Paragraph(f"<b>{k}:</b> {v}", styles['NormalText']))
    elements.append(Spacer(1, 12))
    return elements

def generate_pdf_report(context, sections, images=None):
    tmpfile = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
    doc = SimpleDocTemplate(tmpfile.name, pagesize=A4,
                            rightMargin=2 * cm, leftMargin=2 * cm,
                            topMargin=3 * cm, bottomMargin=2.5 * cm)

    story = []

    # Title page
    story.append(Spacer(1, 4 * cm))
    story.append(Paragraph("Market Intelligence Report", styles['Title']))
    story.append(Spacer(1, 0.2 * cm))
    story.append(Paragraph(f"Focus: {context['input_phrase'].title()}", styles['Heading2']))
    story.append(Spacer(1, 0.5 * cm))
    story.append(Paragraph("Generated dynamically using NLP + LLM + ReportLab", styles['Normal']))
    story.append(PageBreak())

    # Table of Contents
    story.append(Paragraph("TABLE OF CONTENTS", styles['Heading2']))
    toc = [
        "1. Objectives of the Study",
        "2. Market Definition",
        "3. Market Segmentation",
        "4. Stakeholders",
        "5. Executive Summary",
        "6. SWOT Analysis",
        "7. PESTLE Analysis",
        "8. Porter's Five Forces",
        "9. Premium Insights",
        "10. Methodology",
        "11. Appendix"
    ]
    for i, item in enumerate(toc, 1):
        story.append(Paragraph(f"{i}. {item}", styles['NormalText']))
    story.append(PageBreak())

    # Add sections dynamically
    for key, val in sections.items():
        if val:
            title = key.replace('_', ' ').title()
            story += section(title, val)

    # Insert charts/figures
    if images:
        story.append(Paragraph("Visual Insights", styles['SectionHeading']))
        for img_path in images:
            story.append(Image(img_path, width=6*inch, height=3*inch))
            story.append(Spacer(1, 0.2 * inch))
        story.append(PageBreak())

    # Appendix
    story.append(Paragraph("Appendix", styles['SectionHeading']))
    appendix = {
        "Glossary": "CAGR = Compound Annual Growth Rate",
        "Sources": "World Bank, Company Filings, WHO, Transportation Research Board, Expert Interviews",
        "Disclaimer": "All data presented in this report is generated based on public sources and AI-based modeling. For investment or business decisions, consult professional advisors."
    }
    story += section("Appendix Content", appendix)

    # Build the PDF with header/footer
    doc.build(story, onFirstPage=header_footer, onLaterPages=header_footer)
    return tmpfile.name
