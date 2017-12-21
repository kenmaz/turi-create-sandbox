import turicreate as tc

def path2label(path):
    if "reni" in path:
        return "reni"
    elif "kanako" in path:
        return "kanako"
    elif "shiori" in path:
        return "shiori"
    elif "arin" in path:
        return "arin"
    elif "momoka" in path:
        return "momoka"
    else:
        return "unknown"

data = tc.image_analysis.load_images('data/train', with_path=True)
data['label'] = data['path'].apply(path2label)

data.save('faces.sframe')
