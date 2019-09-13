import pandas as pd
from .base_crawler import BaseCrawler
from ..data_source.materials_project.api_helper import VaspCalculated


class MaterialIdCrawler(BaseCrawler):

    def __init__(self):
        super.__init__()

    def _crawl(self):
        MAX_ID = 40000
        MAX_TORELANCE = 5
        fail_cnt = 0
        formula_list = []
        material_id_list = []

        try:
            from fastprogress import progress_bar as pb
            itr = pb(range(MAX_ID))
        except Exception:
            itr = range(MAX_ID)

        for i in itr:
            vc = VaspCalculated()
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

        this._data = pd.DataFrame({
            'material_id': material_id_list,
            'formula': formula_list
        })

        return this._data
