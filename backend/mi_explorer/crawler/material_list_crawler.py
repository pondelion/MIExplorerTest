import pandas as pd
from .base_crawler import BaseCrawler
from ..data_source.materials_project.api_helper import VaspCalculated
from ..utils.logger import Logger


class MaterialListCrawler(BaseCrawler):

    def __init__(self, max_id=40000):
        super(MaterialListCrawler, self).__init__()
        self._MAX_ID = max_id

    def _crawl(self):
        MAX_TORELANCE = 50
        fail_cnt = 0
        formula_list = []
        material_id_list = []

        try:
            from fastprogress import progress_bar as pb
            itr = pb(range(self._MAX_ID))
        except Exception:
            Logger.w(__class__, 'fastprogress is not installed.')
            itr = range(self._MAX_ID)

        vc = VaspCalculated()
        for i in itr:
            res = vc.fetch({'material_specifier': f'mp-{i}', 'property': 'pretty_formula'})
            try:
                formula = res[0]['pretty_formula']
                material_id = res[0]['material_id']
                formula_list.append(formula)
                material_id_list.append(material_id)
                fail_cnt = 0
            except Exception as e:
                fail_cnt += 1
                Logger.e('material_list', f'mp-{i}')
                Logger.e('material_list', e)
            if fail_cnt >= MAX_TORELANCE:
                break

        self._data = pd.DataFrame({
            'material_id': material_id_list,
            'formula': formula_list
        })

        return self._data
