import os
import json

current_dir = os.path.dirname(os.path.realpath(__file__))
PRESETS_DIR = os.path.join(current_dir, "prompt_preset_flies")

if not os.path.exists(PRESETS_DIR):
    os.makedirs(PRESETS_DIR)

def get_all_preset_options():
    if not os.path.isdir(PRESETS_DIR):
        return ["Preset folder not found"]
    
    options = []
    for folder in os.listdir(PRESETS_DIR):
        folder_path = os.path.join(PRESETS_DIR, folder)
        if os.path.isdir(folder_path):
            for file in os.listdir(folder_path):
                if file.endswith('.txt'):
                    file_name = file.replace('.txt', '')
                    options.append(f"{folder}/{file_name}")
    
    return options if options else ["No preset files found"]

def parse_preset_path(preset_path):
    if '/' not in preset_path:
        return None, None
    parts = preset_path.split('/', 1)
    return parts[0], parts[1]

class SystemPromptLoader:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        preset_options = get_all_preset_options()
        
        return {
            "required": {
                "user_prompt": ("STRING", {"multiline": True, "default": ""}),
                "guidance_preset": (preset_options, ),
                "write_user_prompt_to_guidance": ("BOOLEAN", {"default": False}),
            },
            }

    @classmethod
    def OUTPUT_TYPES(cls):
        return ("user_prompt", "system_guidance",)
    RETURN_TYPES = ("STRING", "STRING",)
    RETURN_NAMES = ("user_prompt", "system_guidance",)
    FUNCTION = "load_preset"
    CATEGORY = "zhihui/text"
    OUTPUT_NODE = True

    def load_preset(self, user_prompt, guidance_preset, write_user_prompt_to_guidance):
        system_prompt_content = ""
        
        if guidance_preset in ["Preset folder not found", "No preset files found"]:
            system_prompt_content = "No valid preset file selected."
        else:
            folder, filename = parse_preset_path(guidance_preset)
            if folder and filename:
                file_path = os.path.join(PRESETS_DIR, folder, filename + '.txt')
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        system_prompt_content = f.read()
                except Exception as e:
                    print(f"Error loading preset file {guidance_preset}.txt: {e}")
                    system_prompt_content = f"Error loading preset: {e}"
            else:
                system_prompt_content = "Preset path format error."

        if write_user_prompt_to_guidance and user_prompt:
            final_system_prompt = f"{system_prompt_content}\n{user_prompt}"
        else:
            final_system_prompt = system_prompt_content

        return (user_prompt, final_system_prompt,)