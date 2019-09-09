from flask import Flask, jsonify, request
from flask_cors import CORS
from sklearn.datasets import load_digits
# from umap import UMAP
from sklearn.manifold import TSNE
from mi_explorer.data_source.materials_project.api_helper import VaspCalculated
from mi_explorer.utils.logger import Logger


app = Flask(__name__)
CORS(app)


@app.route('/mock_3d_dist_data', methods=['GET'])
def mock_3d_dist_data():
    digits = load_digits()
    data = digits.data
    label = digits.target
    import numpy as np
    reduced = TSNE(n_components=3).fit_transform(data)
    reduced /= np.percentile(reduced, 90)

    return jsonify({'tag': 'digit',
                    'data': reduced.tolist(),
                    'label': label.tolist()})


@app.route('/test_crystal_structure/<material_key>', methods=['GET'])
def test_crystal_structure(material_key):
    vc = VaspCalculated()
    res = vc.fetch({'material_specifier': material_key, 'property': 'structure'})
    Logger.d('test_crystal_structure', len(res))
    mat = res[0]['structure']['lattice']['matrix']

    return jsonify({'crystal_structure': mat})


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
