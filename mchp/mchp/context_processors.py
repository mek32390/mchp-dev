def max_images(request):
    return { 'MAX_BG_IMAGES' : os.environ.get("MAX_BG_IMAGES", "1") }

