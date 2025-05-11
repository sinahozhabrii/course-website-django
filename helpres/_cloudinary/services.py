from django.template.loader import get_template
from config import settings

def get_cloudinary_image_obj(instance,as_html=False,width=500,field_name='image'):

    if not hasattr(instance,field_name):
        return ""
    image_obj = getattr(instance,field_name)
    if not image_obj:
        return ""

    image_options = {
        'width':width
    }
    if as_html:
        return image_obj.image(**image_options)
    url = image_obj.build_url(**image_options)
    return url

def get_cloudinary_video_obj(instance,as_html=False,width=500,field_name='video',height=None,fetch_format="auto",quality="auto",sign_url=False):

    if not hasattr(instance,field_name):
        return ""
    video_obj = getattr(instance,field_name)
    if not video_obj:
        return ""

    video_options = {
        "fetch_format":fetch_format,
        "quality":quality,
        "sign_url":sign_url
    }
    if height is not None:
        video_options['height'] = height
    if width is not None :
        video_options['width'] = width
    if height and width:
        video_options['crop'] = 'limit'
    url = video_obj.build_url(**video_options)
    if as_html:
        template_name = 'video/embed/embed.html'
        template = get_template(template_name)
        cloud_name = settings.CLOUD_NAME
        _html = template.render({'video_url':url,'cloud_name':cloud_name})
        return _html
    return url