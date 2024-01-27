
nrrd_directory = '/usr/sci/scratch/Moksha/femur_newdata/new_data/train/segmentations'
nifti_directory = '/usr/sci/scratch/rachaell/raw_datasets/Femur/labelsTr'
i=0
    
# Iterate through all items in the base directory
for nrrd_file in os.listdir(nrrd_directory):
    nrrd_file_path = os.path.join(nrrd_directory, nrrd_file)

    # Read the .nrrd file
    nrrd_data, nrrd_header = nrrd.read(nrrd_file_path)
    nifti_img = nib.Nifti1Image(nrrd_data, affine=np.eye(4))

    # Correct the file extension and add the missing path separator
    save_nifti_path = os.path.join(nifti_directory, os.path.basename(nrrd_file_path)[:-5] + '.nii.gz')
    print(save_nifti_path)
    nib.save(nifti_img, save_nifti_path)
