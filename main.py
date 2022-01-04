import data_handling
import pca

# Analyze and display only pharmaceutical compounds that target a specific organ system.
system_specific = False

# Analyze only compounds that have reached clinical research phase 3 or 4.
phase_selection = False

if __name__ == '__main__':
    cleaned_dataset_path = data_handling.clean_data(system_specific)
    pca_outputs = pca.run(cleaned_dataset_path)
    pca.scatter_plot(pca_outputs, phase_selection)
