# ✅ pdf_template.py — Styled PDF Export with ReportLab

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Frame, PageTemplate
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from datetime import datetime

# === GLOBAL CONFIG ===
PAGE_WIDTH, PAGE_HEIGHT = A4
MARGIN = 0.75 * inch
styles = getSampleStyleSheet()

# === CUSTOM HEADER & FOOTER ===
def header_footer(canvas, doc):
    canvas.saveState()
    canvas.setFont('Helvetica-Bold', 10)
    canvas.drawString(MARGIN, PAGE_HEIGHT - 0.5 * inch, f"Market Intelligence Report")
    canvas.drawRightString(PAGE_WIDTH - MARGIN, PAGE_HEIGHT - 0.5 * inch, datetime.today().strftime("%B %d, %Y"))

    canvas.setFont('Helvetica', 9)
    canvas.setStrokeColor(colors.grey)
    canvas.line(MARGIN, 0.75 * inch, PAGE_WIDTH - MARGIN, 0.75 * inch)
    canvas.drawRightString(PAGE_WIDTH - MARGIN, 0.5 * inch, f"Page {doc.page}")
    canvas.restoreState()

# === MAIN EXPORT FUNCTION ===
def generate_pdf_report(context, sections):
    filename = "Styled_Market_Report.pdf"
    doc = SimpleDocTemplate(
        filename,
        pagesize=A4,
        leftMargin=MARGIN,
        rightMargin=MARGIN,
        topMargin=1.2 * inch,
        bottomMargin=1 * inch
    )

    story = []

    # Section title style
    title_style = ParagraphStyle(
        name='SectionTitle', parent=styles['Heading2'], fontSize=14, spaceAfter=10, textColor=colors.HexColor("#003366")
    )

    body_style = ParagraphStyle(
        name='BodyText', parent=styles['BodyText'], fontSize=11, leading=16
    )

    # Add Executive Summary
    story.append(Paragraph("Executive Summary", title_style))
    story.append(Paragraph(sections.get("executive_summary", "Not available."), body_style))
    story.append(Spacer(1, 0.2 * inch))

    # Add SWOT
    story.append(Paragraph("SWOT Analysis", title_style))
    story.append(Paragraph(sections.get("swot", "Not available."), body_style))
    story.append(Spacer(1, 0.2 * inch))

    # Add PESTLE
    story.append(Paragraph("PESTLE Analysis", title_style))
    story.append(Paragraph(sections.get("pestle", "Not available."), body_style))
    story.append(Spacer(1, 0.2 * inch))

    # Add Porter's
    story.append(Paragraph("Porter's Five Forces", title_style))
    story.append(Paragraph(sections.get("porter", "Not available."), body_style))
    story.append(PageBreak())

    # Add Table of Contents (just an example placeholder)
    story.append(Paragraph("Appendix", title_style))
    story.append(Paragraph("Glossary, Sources, and Notes appear here.", body_style))

    # Add Page Template with Header/Footer
    doc.build(story, onFirstPage=header_footer, onLaterPages=header_footer)

    return filename
