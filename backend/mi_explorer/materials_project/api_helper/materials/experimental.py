from ..base_api_helper import BaseApiHelper


class Experimental(BaseApiHelper):

    def __init__(self):
        super().__init__()

    def _get_api_url_fmt(self):
        return 'https://www.materialsproject.org/rest/v2/materials/{material_specifier}/exp'
