1. DICOM Files .dcm
* 2D Slices

2. NIfTI Files .nii.gz
* 3D Volumes

3.MetaImage .mhd and .raw
* **.mhd (Meta Header File)**: 
   - The `.mhd` file is a small text file that contains metadata about the medical image. 
   - This metadata includes information such as the dimensions of the image, data type, data encoding, size of the image, and other details necessary to interpret the image data correctly.
   - It acts as a header file and does not contain the actual image data.

* **.raw (Raw Image Data File)**:
   - The `.raw` file contains the actual image data in a raw, unprocessed format.
   - This file is typically large as it holds the image pixel values without any compression or formatting.
   - The `.raw` file is usually read in conjunction with the `.mhd` file, which provides the necessary information to correctly interpret the raw data.

Together, these files are used to store high-resolution medical images such as CT scans, MRI scans, or other volumetric data. The separation of metadata from the image data allows for flexibility and efficiency in processing and analyzing medical images. The MetaImage format is widely supported by various medical imaging software and tools, making it a standard choice in medical image processing and analysis.
