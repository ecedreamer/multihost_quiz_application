from rest_framework import renderers



class CustomJsonRenderer(renderers.JSONRenderer):
    media_type = 'application/json'
    format = 'json'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        success = 200 <= renderer_context.get("response").status_code <= 299
        base_data = {
            "success": success,
            "data": data
        }
        return super().render(base_data, accepted_media_type, renderer_context)