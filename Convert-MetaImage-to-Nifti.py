'''
This code converts medical images stored in MetaImage format i.e. .mhd and .raw files to Nifti format
-> Assumes that all .md and .raw files are in the same folder
-> Assumes that corresponding .mhd and .raw files will have the same name
'''
import os
import pydicom
import numpy as np
import nibabel as nib
import SimpleITK as sitk

def convert_mhd_to_nii_gz(mhd_file_path, output_file_path):
    # Read the image using the .mhd file
    image = sitk.ReadImage(mhd_file_path)

    # Write the image in NIfTI format (.nii.gz)
    sitk.WriteImage(image, output_file_path, True)  # The third argument 'True' enables compression


directory = '/usr/sci/scratch/rachaell/raw_datasets/SLiver07/scan'

i=1
# Iterate over all files in the directory
for filename in os.listdir(directory):
    if filename.endswith('.mhd'):
        # Construct full file path
        mhd_file_path = os.path.join(directory, filename)
        # Construct output file path (change .mhd to .nii.gz)
        output_file_path = os.path.join(f'/usr/sci/scratch/rachaell/raw_datasets/SLiver07/nifti-slices/sliver_{i:04}.nii.gz')

        # Convert the file
        convert_mhd_to_nii_gz(mhd_file_path, output_file_path)
        print(f"Converted {filename} to NIfTI format")
        i=i+1
