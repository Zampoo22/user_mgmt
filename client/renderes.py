from rest_framework.renderers import JSONRenderer
class SuccessJSONRender(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        try:
            action = (renderer_context['view'].action)
        except AttributeError:
            action = 'retrive'
        if 'detail' not in data:
            status_code = renderer_context['response'].status_code
            success_data = {
                'status_code': status_code,
                'message': f"Data is Succesfully {action}ed",
                'data': data
            }
            return super().render(success_data, accepted_media_type, renderer_context)
        return super().render(data, accepted_media_type, renderer_context)
    