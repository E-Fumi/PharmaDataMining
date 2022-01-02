import data_handling
import pca

# Analyze and display only pharmaceutical compounds that target a specific organ system.
system_specific = True

# Analyze only compounds that have reached clinical research phase 3 or 4.
phase_selection = True

if __name__ == '__main__':
    cleaned_dataset = data_handling.clean_data(system_specific)
    pca_outputs = pca.run(cleaned_dataset)
    pca.scatter_plot(pca_outputs, phase_selection)
