from typing import Optional
from comfy import utils

class MultiLineTextNode:
    CATEGORY = "zhihui/text"
    OUTPUT_NODE = True
    
    def __init__(self):
        self.comment = ""
        self.content = ""
        
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "comment": ("STRING", {"default": "", "multiline": False}),
                "enable": ("BOOLEAN", {"default": True}), 
                "text": ("STRING", {"default": "", "multiline": True}),
            }
        }
     
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text_output",)
    FUNCTION = "execute"
    
    def execute(self, comment: str, text: str, enable: bool) -> tuple:
        self.comment = comment
        self.content = text
        if not enable:
            return ("",) 
        return (text,)