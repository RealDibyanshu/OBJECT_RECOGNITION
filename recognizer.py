from imageai.Detection import ObjectDetection
import os

# Instantiating the class
recognizer = ObjectDetection()

# Defining the paths
path_model = "./Models/yolo-tiny.h5"
input_folder = "./Input/"
output_folder = "./Output/"

# Using the setModelTypeAsTinyYOLOv3() function
recognizer.setModelTypeAsTinyYOLOv3()

# Setting the path of the Model
recognizer.setModelPath(path_model)

# Loading the model
try:
    recognizer.loadModel()
except Exception as e:
    print(f"Error loading the model: {e}")
    exit()

# Iterate through input images
for input_file in os.listdir(input_folder):
    if input_file.endswith(".jpg") or input_file.endswith(".png"):
        input_path = os.path.join(input_folder, input_file)
        output_path = os.path.join(output_folder, f"output_{input_file}")

        # Calling the detectObjectsFromImage() function
        recognition = recognizer.detectObjectsFromImage(
            input_image=input_path,
            output_image_path=output_path
        )

        # Iterating through the items found in the image
        print(f"Objects detected in {input_file}:")
        for eachItem in recognition:
            print(f"{eachItem['name']} : {eachItem['percentage_probability']}")

        print(f"Output image saved at: {output_path}\n")
from imageai.Detection import ObjectDetection
import os

# Instantiating the class
recognizer = ObjectDetection()

# Defining the paths
path_model = "./Models/yolo-tiny.h5"
input_folder = "./Input/"
output_folder = "./Output/"

# Using the setModelTypeAsTinyYOLOv3() function
recognizer.setModelTypeAsTinyYOLOv3()

# Setting the path of the Model
recognizer.setModelPath(path_model)

# Loading the model
try:
    recognizer.loadModel()
except Exception as e:
    print(f"Error loading the model: {e}")
    exit()

# Iterate through input images
for input_file in os.listdir(input_folder):
    if input_file.endswith(".jpg") or input_file.endswith(".png"):
        input_path = os.path.join(input_folder, input_file)
        output_path = os.path.join(output_folder, f"output_{input_file}")

        # Calling the detectObjectsFromImage() function
        recognition = recognizer.detectObjectsFromImage(
            input_image=input_path,
            output_image_path=output_path
        )

        # Iterating through the items found in the image
        print(f"Objects detected in {input_file}:")
        for eachItem in recognition:
            print(f"{eachItem['name']} : {eachItem['percentage_probability']}")

        print(f"Output image saved at: {output_path}\n")
