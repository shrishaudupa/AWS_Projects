from django.shortcuts import render


import torch
from PIL import Image
from transformers import VisionEncoderDecoderModel, ViTImageProcessor, AutoTokenizer
from torch.utils.data import Dataset, DataLoader

from django.core.files.storage import FileSystemStorage

model_name = "nlpconnect/vit-gpt2-image-captioning"
model = VisionEncoderDecoderModel.from_pretrained(model_name)

# Load the feature extractor (image processor) and tokenizer
feature_extractor = ViTImageProcessor.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Set up the device (GPU or CPU)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

# Define a custom dataset class for images
class ImageDataset(Dataset):
    def __init__(self, image_paths, captions):
        self.image_paths = image_paths
        self.captions = captions

    def __len__(self):
        return len(self.image_paths)

    def __getitem__(self, idx):
        image_path = self.image_paths[idx]
        caption = self.captions[idx]

        # Load the image
        image = Image.open(image_path).convert("RGB")

        # Extract image features
        pixel_values = feature_extractor(images=image, return_tensors="pt").pixel_values.squeeze(0)

        # Tokenize caption
        encoded_caption = tokenizer(caption, padding="max_length", max_length=30, truncation=True, return_tensors="pt")

        return {
            "pixel_values": pixel_values,
            "input_ids": encoded_caption["input_ids"].squeeze(0),
            "attention_mask": encoded_caption["attention_mask"].squeeze(0),
        }

# Define image paths and captions
image_paths = [
    "C:\\Users\\SriLakshmi Udupa\\Downloads\\IMG_20240719_123447.jpg",
    "C:\\Users\\SriLakshmi Udupa\\Downloads\\IMG_20241004_082326.jpg",
]
captions = ["A beautiful sunset over the beach.", "A cat sitting on a windowsill."]

# Create dataset and data loader
dataset = ImageDataset(image_paths, captions)
data_loader = DataLoader(dataset, batch_size=2, shuffle=True)

def generate_caption(image_path):
    # Load the image
    image = Image.open(image_path).convert("RGB")

    # Process the image
    pixel_values = feature_extractor(images=image, return_tensors="pt").pixel_values.to(device)

    # Generate caption
    model.eval()
    with torch.no_grad():
        output_ids = model.generate(pixel_values, max_length=20, num_beams=5)

    # Decode the generated caption
    caption = tokenizer.decode(output_ids[0], skip_special_tokens=True)
    return caption
def homepage(request):
    caption = ""
    image_url = ""

    if request.method == "POST" and request.FILES.get("image"):
        uploaded_image = request.FILES["image"]
        
        # Save the uploaded image
        fs = FileSystemStorage()
        filename = fs.save(uploaded_image.name, uploaded_image)
        image_path = fs.path(filename)  # Get full file path
        image_url = fs.url(filename)    # URL to access the image

        # Generate a caption for the uploaded image
        caption = generate_caption(image_path)

    return render(request, "html/homepage.html", {"caption": caption, "image_url": image_url})




