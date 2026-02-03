import os

directory = r'D:\coding\html games\Phonics\js\audio_mp3'

for filename in os.listdir(directory):
    if filename.startswith('__'):
        # Target: __A bee is in the cone._,.mp3 -> A bee is in the cone.mp3
        # Remove leading __
        new_name = filename[2:]
        
        # Remove trailing characters before extension
        # e.g. ._,.mp3 or ._.mp3
        base, ext = os.path.splitext(new_name)
        
        # Strip trailing punctuation/underscores from the base name
        # We want to keep the text as it is in data.js excluding the final period.
        # Looking at data.js: "A bee is in the cone." 
        # So we want "A bee is in the cone.mp3"
        
        cleaned_base = base.rstrip('_,. ')
        
        new_filename = cleaned_base + ext
        
        old_path = os.path.join(directory, filename)
        new_path = os.path.join(directory, new_filename)
        
        print(f"Renaming: {filename} -> {new_filename}")
        try:
            os.rename(old_path, new_path)
        except OSError as e:
            print(f"Error renaming {filename}: {e}")
