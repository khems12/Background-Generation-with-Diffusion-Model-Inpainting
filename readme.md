# Background Generation with Diffusion Model Inpainting

This project implements a background generation system using a diffusion-based inpainting model. It allows users to upload images and generate new backgrounds by modifying the original image's background while preserving the foreground. This is particularly useful for creating new scenes or adjusting backgrounds while maintaining the integrity of the main subject.

## Features
- Background removal using a mask.
- Background regeneration with diffusion inpainting.
- Adjustable inpainting parameters for fine-tuning the results.

## Demo
A live demo is available at: [HuggingFace Space](https://huggingface.co/spaces/akashmaurya/bg_generator)


## Table of Contents
- [Usage](#usage)
- [Challenges Faced](#challenges-faced)

---
## Usages

- Upload any image and get the background generated based on the prompt

### Diffusion Model Inpainting

The project uses a diffusion model for inpainting, which regenerates the background while preserving the quality of the foreground. The process follows these steps:

- Mask Generation: A mask is generated to separate the background from the foreground.
- Diffusion Inpainting: The diffusion model inpaints the background, replacing the masked areas as per the prompt. 

### Code Structure

`app.py`: Contains the Streamlit-based user interface for image upload, mask generation, and background regeneration.

`main.py`: Core logic for handling diffusion inpainting and mask manipulation.

`requirements.txt`: Python dependencies required for running the project.

## Challenges Faced 

### Mask Generation
One of the primary challenges was generating a perfect mask for the background. Accurately separating the foreground from the background required fine-tuning image segmentation techniques. Small inaccuracies in the mask resulted in artifacts in the inpainted image.

### Inpainting Parameters
Another challenge was adjusting the inpainting parameters. Different images required different settings for optimal results. Tuning parameters such as the diffusion steps, noise levels, and mask areas required trial and error to balance foreground preservation and background regeneration.

#### Note:

The deployed model is running on the `HuggingFace Free Space` with the CPU Basic 2vCPU 16 GB RAM. The image genration will take longer time and to give the results.

For faster inference use the `generate_bg.ipynb` note with colab free T4 GPU. 
