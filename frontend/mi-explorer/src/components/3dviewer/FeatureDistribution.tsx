import React from 'react';
import request from 'superagent';
import * as THREE from 'three';
import ThreeScene from './ThreeScene';
import { Props as ThreeProps, ThreeObjects } from './ThreeScene';
import { ObjectFactory as OF } from '../../utils/three/ObjectFactory';


type Props= ThreeProps;

class FeatureDistribution extends ThreeScene {

  private _data = [];
  private _label = [];
  private _cnt: number = 0;

  constructor(props: Props) {
    super(props);

    this.animate = this.animate.bind(this);
    this.createObjects = this.createObjects.bind(this);

    request
      .get('http://127.0.0.1:5000/mock_3d_dist_data')
      .end((err, res) => {
        if (err) {
          console.log(err);
          return;
        }

        this._data = res.body.data;
        this._label = res.body.label;
        //window.alert(this._label);

        this._objects = this.createObjects();
        this.onObjectsUpdated();

        this.forceUpdate();
      })
  }

  createObjects(): ThreeObjects {
    const COLORS: number[] = [
      0xB71C1C, 0x880E4F, 0x4A148C, 0x311B92, 0x1A237E, 0x0D47A1,
      0x006064, 0x1B5E20, 0x827717, 0xFF6F00, 0xBF360C, 0xEEEEEE,
    ]

    const cols = this._label.map((label: number) => {
        return COLORS[label]
    });

    return this._data.map((data: number[], idx: number) => {
      //console.log(data);
      return {
        tag: 'points1',
        obj: OF.createSprite(data[0], data[1], data[2], 0.05, cols[idx]),
        objType: 'sprite'
      }
    })
  }

  animate(): void {
    this._cnt += 1;
    this._camera.position.x = 3.0 * Math.cos(0.01 * this._cnt);
    this._camera.position.z = 3.0 * Math.sin(0.01 * this._cnt);
    this._camera.lookAt(new THREE.Vector3(0, 0, 0));
    super.animate();
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
