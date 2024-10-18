from PIL import Image, ImageDraw, ImageFont

def create_infographic(summary_data, output_image):
    # Create a blank white image
    img = Image.new('RGB', (800, 1000), color=(255, 255, 255))
    d = ImageDraw.Draw(img)

    # Load a font
    font = ImageFont.load_default()

    # Add text to the image
    d.text((10, 10), "Client Name: {}".format(summary_data.get('ClientName', 'N/A')), font=font, fill=(0, 0, 0))
    d.text((10, 50), "Financial Well Being: {}".format(summary_data.get('FinancialWellBeing', 'N/A')), font=font, fill=(0, 0, 0))
    d.text((10, 90), "Key Wins: {}".format(summary_data.get('KeyWins', 'N/A')), font=font, fill=(0, 0, 0))
    # Add other sections...

    # Save the image
    img.save(output_image)

# Create the infographic
output_image = 'summary.png'
create_infographic(summary_data, output_image)