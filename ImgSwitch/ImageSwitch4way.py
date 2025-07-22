import comfy
import comfy.sd
import comfy.utils
import torch

class ImageSwitch4way:
        
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image1_comment": ("STRING", {"multiline": False, "default": ""}),
                "image2_comment": ("STRING", {"multiline": False, "default": ""}),
                "image3_comment": ("STRING", {"multiline": False, "default": ""}),
                "image4_comment": ("STRING", {"multiline": False, "default": ""})
            },
            "optional": {
                "image1": ("IMAGE", {}),
                "image2": ("IMAGE", {}),
                "image3": ("IMAGE", {}),
                "image4": ("IMAGE", {}),
                "select_image": (["1", "2", "3", "4"], {"default": "1"})
            }
        }

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("output_image",)
    FUNCTION = "execute"
    CATEGORY = "zhihui/image"

    def execute(self, image1_comment, image2_comment, image3_comment, image4_comment, image1=None, image2=None, image3=None, image4=None, select_image="1"):
        images = [image1, image2, image3, image4]
        idx = int(select_image)-1
        if idx < 0 or idx > 3:
            return (None,)
        if images[idx] is None:
            return (None,)
        return (images[idx],)