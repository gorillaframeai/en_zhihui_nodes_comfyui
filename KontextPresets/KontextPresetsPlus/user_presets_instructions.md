# User Preset File Usage Instructions

## Overview

The `user_presets.txt` file allows you to create and manage your own custom presets, which will be displayed alongside default presets in the node interface.

## File Format

The user preset file uses JSON format with the following structure:

```json
{
  "preset_collection": [
    {
      "name": "Preset Name",
      "brief": "Detailed description or instructions for the preset"
    },
    {
      "name": "Personal Art Style",
      "brief": "Transform the image into my personal artistic style with vibrant colors, dynamic composition, and expressive brushstrokes that capture emotion and movement."
    }
  ]
}
```

## Usage

1. **Edit preset file**: Directly edit the `user_presets.txt` file
2. **Add new presets**: Add new preset objects to the `preset_collection` array
3. **Modify existing presets**: Directly modify the `name` or `brief` fields of corresponding presets
4. **Save file**: Ensure the file is saved with UTF-8 encoding

## Display Effect

- Default presets display as: `[Default] Preset Name`
- User presets display as: `[User] Preset Name`

## Notes

1. **JSON format**: Ensure the file conforms to JSON format specifications
2. **Encoding format**: File must be saved with UTF-8 encoding
3. **Special characters**: Special characters in JSON need to be escaped
4. **Backup file**: Recommend backing up the original file before modifications

## Example Presets

The file already contains example presets that you can reference to create your own presets.

## Error Handling

If the user preset file has format errors or doesn't exist, the system will:
- Display corresponding error messages
- Continue loading default presets
- Not affect normal node usage