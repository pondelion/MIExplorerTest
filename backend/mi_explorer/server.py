from flask import Flask, jsonify, request
from sklearn.datasets import load_digits
# from umap import UMAP
from sklearn.manifold import TSNE


app = Flask(__name__)


@app.route('/mock_3d_dist_data', methods=['GET'])
def mock_3d_dist_data():
    digits = load_digits()
    data = digits.data
    label = digits.target
    reduced = TSNE(n_components=3).fit_transform(data)

    return jsonify({'tag': 'digit',
                    'data': reduced.tolist(),
                    'label': label.tolist()})


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
