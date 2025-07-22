import comfy
import comfy.sd
import comfy.utils
import torch

class TextSwitch:
        
    def __init__(self):
        self.text_cache = {"text1": "", "text2": "", "text3": "", "text4": ""}

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "optional": {
                "text1": ("STRING", {"multiline": True, "default": "", "forceInput": True}),
                "text2": ("STRING", {"multiline": True, "default": "", "forceInput": True}),
                "text3": ("STRING", {"multiline": True, "default": "", "forceInput": True}),
                "text4": ("STRING", {"multiline": True, "default": "", "forceInput": True})
            },
            "required": {
                "text1_comment": ("STRING", {"multiline": False, "default": ""}),
                "text2_comment": ("STRING", {"multiline": False, "default": ""}),
                "text3_comment": ("STRING", {"multiline": False, "default": ""}),
                "text4_comment": ("STRING", {"multiline": False, "default": ""}),
                "select_text": (["1", "2", "3", "4"], {"default": "1"})
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text_output",)
    FUNCTION = "execute"
    CATEGORY = "zhihui/text"

    def execute(self, text1_comment, text2_comment, text3_comment, text4_comment, select_text, text1="", text2="", text3="", text4=""):
        self.text_cache["text1"] = text1
        self.text_cache["text2"] = text2
        self.text_cache["text3"] = text3
        self.text_cache["text4"] = text4
        prompts = [text1, text2, text3, text4]
        return (prompts[int(select_text)-1],)