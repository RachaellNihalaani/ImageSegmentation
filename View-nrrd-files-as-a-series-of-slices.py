import nrrd
import matplotlib.pyplot as plt
import ipywidgets as widgets
from IPython.display import display

# Replace with your .nrrd file path
nrrd_file_path = '/usr/sci/scratch/Moksha/femur_newdata/new_data/train/images/N05_51053_L_femur_1x_hip.isores.padded.com.aligned.cropped.nrrd'

# Read the .nrrd file
nrrd_data, nrrd_header = nrrd.read(nrrd_file_path)

# Function to display a slice
def display_slice(slice_num):
    plt.imshow(nrrd_data[:, :, slice_num], cmap='gray')
    plt.title(f'Slice number: {slice_num}')
    plt.axis('off')
    plt.show()

# Create a slider to navigate through slices
slice_slider = widgets.IntSlider(
    value=nrrd_data.shape[2] // 2,
    min=0,
    max=nrrd_data.shape[2] - 1,
    step=1,
    description='Slice:',
    continuous_update=False
)

# Display the widget
widgets.interactive(display_slice, slice_num=slice_slider)
