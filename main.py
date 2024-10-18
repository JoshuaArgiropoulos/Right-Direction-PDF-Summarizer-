import os
from extract import extract_data_from_pptx
from summary import create_summary_pdf
from infographic import create_infographic

def main():
    agendas_folder = 'Agendas'  # Folder containing the PPTX files
    output_folder = 'output'     # Folder to save the output files

    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    pptx_files = [f for f in os.listdir(agendas_folder) if f.endswith('.pptx')]
    
    for pptx_file in pptx_files:
        pptx_path = os.path.join(agendas_folder, pptx_file)
        print(f'Processing {pptx_file}...')
        
        try:
            summary_data = extract_data_from_pptx(pptx_path)
            
            # Create PDF summary
            pdf_file_name = f'summary_{pptx_file[:-5]}.pdf'
            create_summary_pdf(summary_data, os.path.join(output_folder, pdf_file_name))
            
            # Create infographic (if still needed)
            infographic_file_name = f'summary_{pptx_file[:-5]}.png'
            create_infographic(summary_data, os.path.join(output_folder, infographic_file_name))
            
            print(f'Successfully processed {pptx_file}.')
        except Exception as e:
            print(f'An error occurred while processing {pptx_file}: {e}')

            
# Call the main function
if __name__ == "__main__":
    main()