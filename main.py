def main(pptx_file):
    summary_data = extract_data_from_pptx(pptx_file)
    
    # Create text summary
    create_summary_text(summary_data, 'summary.txt')
    
    # Create infographic
    create_infographic(summary_data, 'summary.png')

# Call the main function with the path to the PowerPoint file
if __name__ == "__main__":
    main('path_to_your_pptx_file.pptx')