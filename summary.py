from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image

def create_summary_pdf(summary_data, output_file):
    pdf = SimpleDocTemplate(output_file, pagesize=letter)
    styles = getSampleStyleSheet()

    # Custom styles for the PDF
    title_style = styles['Title']
    normal_style = styles['Normal']
    normal_style.leading = 14  # Set line spacing

    # Create a list to hold the content
    content = []

    # Title
    content.append(Paragraph("Client Summary", title_style))
    content.append(Spacer(1, 12))

    # Add each section of the summary data
    for key, value in summary_data.items():
        content.append(Paragraph(f"<b>{key.replace('_', ' ')}:</b> {value}", normal_style))
        content.append(Spacer(1, 6))  # Add space between paragraphs

    # Build the PDF
    pdf.build(content)