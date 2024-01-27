import os
from PIL import Image
import numpy as np
import nibabel as nib
def png_to_array(png_file_path):
    # Load PNG image
    png_image = Image.open(png_file_path)
    return np.array(png_image)

def save_nifti(volume, filename):
    volume = volume.astype(np.float32)
    # Convert the numpy array to a NIfTI image
    nifti_img = nib.Nifti1Image(volume, affine=np.eye(4))
    # Save the NIfTI image
    nib.save(nifti_img, filename)

# Directory containing PNG files
png_folder_path = '/usr/sci/scratch/rachaell/raw_datasets/CHAOS/CHAOS_Train_Sets/CT/23/Ground'

# Read and convert each PNG file to an array
image_arrays = []
for png_file in sorted(os.listdir(png_folder_path)):
    if png_file.lower().endswith('.png'):
        png_file_path = os.path.join(png_folder_path, png_file)
        image_array = png_to_array(png_file_path)
        image_arrays.append(image_array)

# Stack the image arrays to create a 3D array
stacked_images = np.stack(image_arrays, axis=0)
save_nifti(stacked_images, '/usr/sci/scratch/rachaell/raw_datasets/CHAOS/labelsTr/chaos_23.nii.gz')

# Now stacked_images is a 3D numpy array representing the stack of images
