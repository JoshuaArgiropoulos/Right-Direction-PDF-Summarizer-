def create_summary_text(summary_data, output_file):
    with open(output_file, 'w') as f:
        f.write("Client Name: {}\n".format(summary_data.get('ClientName', 'N/A')))
        f.write("Financial Well Being: {}\n".format(summary_data.get('FinancialWellBeing', 'N/A')))
        f.write("Key Wins: {}\n".format(summary_data.get('KeyWins', 'N/A')))
        # Add other sections as needed
        f.write("\nGoals: {}\n".format(summary_data.get('Goals', 'N/A')))
        f.write("\nEstate Planning: {}\n".format(summary_data.get('EstatePlanning', 'N/A')))
        # Continue for all other sections

# Create the summary
output_file = 'summary.txt'
create_summary_text(summary_data, output_file)