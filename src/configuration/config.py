InputFolderPath = "inputFolder"
DEVICE = 'cpu'
AVAILABLE_MODELS = {'u', 'g'}
AVAILABLE_TEMPLATES = {
    'T1w_1mm': 'MNI152_T1_1mm_Brain.nii.gz', 
    'T1w_2mm': 'MNI152_T1_2mm_Brain.nii.gz', 
    'T2w_1mm': 'MNI152_T2_1mm_Brain.nii.gz',
}
checkpointDir = "checkpoints"
preprocess_output_path = "preprocessed_files"
template_path = "templates/MNI152_T1_1mm_Brain.nii.gz"
stripping_model_path = "synthstrip.pt"

ants_bin = "ants_2_6_3/ants-2.6.3/bin"