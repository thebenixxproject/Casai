from diffusers import StableDiffusionPipeline
import torch
import os

# Configuración del modelo
model_id = "runwayml/stable-diffusion-v1-5"
device = "cuda" if torch.cuda.is_available() else "cpu"
pipe = StableDiffusionPipeline.from_pretrained(model_id)
pipe = pipe.to(device)

# Ruta para guardar las imágenes
save_path = r"C:\Users\Admin\Desktop\AI Photos"
os.makedirs(save_path, exist_ok=True)  # Crear la carpeta si no existe

# Pedir al usuario el texto para generar la imagen
prompt = input("Una pintura al óleo de una tormenta en el mar.")

# Generar la imagen
image = pipe(prompt).images[0]

# Determinar el siguiente número para el nombre del archivo
existing_files = os.listdir(save_path)
numbers = [
    int(file.split('.')[0]) for file in existing_files if file.split('.')[0].isdigit()
]
next_number = max(numbers) + 1 if numbers else 1  # Si no hay archivos, empezar en 1

# Guardar la imagen con un nombre numerado
file_name = f"{next_number}.png"
image.save(os.path.join(save_path, file_name))

# Mostrar mensaje de éxito
print(f"Imagen generada y guardada como {file_name} en {save_path}.")
