from rest_framework.renderers import JSONRenderer
class SuccessJSONRender(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        try:
            action = (renderer_context['view'].action)
        except AttributeError:
            action = 'retrive'
        
        action = action[:-1] if action[-1] == 'e' else action
        message = f"Data is succesfully {action}ed"

        if 'detail' in data:
            message = f"An error occured."

        status_code = renderer_context['response'].status_code
        success_data = {
            'status_code': status_code,
            'message': message,
            'data': data
        }
        return super().render(success_data, accepted_media_type, renderer_context)
    