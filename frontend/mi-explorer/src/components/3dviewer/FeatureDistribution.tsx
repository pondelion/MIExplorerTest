import React from 'react';
import request from 'superagent';
import ThreeScene from './ThreeScene';
import { Props as ThreeProps } from './ThreeScene';


type Props= ThreeProps;

class FeatureDistribution extends ThreeScene {

  private _data = null;
  private _label = null;

  constructor(props: Props) {
    super(props);

    request
      .get('http://127.0.0.1:5000/mock_3d_dist_data')
      .end((err, res) => {
        if (err) {
          console.log(err);
          return;
        }

        this._data = res.body.data;
        this._label = res.body.data;
        window.alert(this._label);
        this.forceUpdate();
      })
  }

  render() {
    return (
      <div>
        {super.render()}
        {this._data}
      </div>
    )
  }
}

export default FeatureDistribution;
