from flask import Flask, jsonify, request
from flask_cors import CORS
from sklearn.datasets import load_digits
# from umap import UMAP
from sklearn.manifold import TSNE
from mi_explorer.data_source.materials_project.api_helper import VaspCalculated
from mi_explorer.utils.logger import Logger


app = Flask(__name__)
CORS(app)


@app.route('/mock_dist_data/<dim>', methods=['GET'])
def mock_dist_data(dim):
    dim = int(dim)
    digits = load_digits()
    data = digits.data
    label = digits.target
    import numpy as np
    reduced = TSNE(n_components=dim).fit_transform(data)
    reduced /= np.percentile(reduced, 90)

    return jsonify({'tag': 'digit',
                    'data': reduced.tolist(),
                    'label': label.tolist()})


@app.route('/test_crystal_structure/<material_key>', methods=['GET'])
def test_crystal_structure(material_key):
    vc = VaspCalculated()
    res = vc.fetch({'material_specifier': material_key, 'property': 'structure'})
    Logger.d('test_crystal_structure', len(res))
    mat = res[2]['structure']['lattice']['matrix']
    sites = {}
    for site in res[2]['structure']['sites']:
        if site['species'][0]['element'] not in sites:
            sites[site['species'][0]['element']] = []
        sites[site['species'][0]['element']].append(site['xyz'])

    return jsonify({'matrix': mat,
                    'sites': sites})


@app.route('/vasp/material_list', methods=['GET'])
def material_list():
    MAX_ID = 400
    MAX_TORELANCE = 5
    fail_cnt = 0
    formula_list = []
    material_id_list = []
    for i in range(MAX_ID):
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

    return jsonify({'formula': formula_list,
                    'material_id': material_id_list})


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
