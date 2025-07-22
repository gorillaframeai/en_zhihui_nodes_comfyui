import torch

class AutoImageSwitch:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {},
            "optional": {
                "image_a": ("IMAGE", {}),
                "image_b": ("IMAGE", {}),
                "image_c": ("IMAGE", {})
            }
        }

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("output_image",)
    FUNCTION = "execute"
    CATEGORY = "zhihui/image"

    def execute(self, image_a=None, image_b=None, image_c=None):
        # Return first available image (priority: A -> B -> C)
        if image_a is not None:
            return (image_a,)
        elif image_b is not None:
            return (image_b,)
        elif image_c is not None:
            return (image_c,)
        else:
            # Return empty image if no inputs
            empty_image = torch.zeros(1, 512, 512, 3, dtype=torch.float32)
            return (empty_image,)