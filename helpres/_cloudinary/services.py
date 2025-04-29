def get_image_thumbnail(instance,as_html=False,width=500,field_name='image'):

    if not hasattr(instance,field_name):
        return ""
    image_obj = getattr(instance,field_name)
    if not image_obj:
        return ""

    image_options = {
        'width':width
    }
    if as_html:
        return image_obj.image.image(**image_options)
    url = image_obj.image.build_url(**image_options)
    return url