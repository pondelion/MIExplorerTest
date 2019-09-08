import React from 'react';
import request from 'superagent';
import * as THREE from 'three';
import ThreeScene from './ThreeScene';
import { Props as ThreeProps, ThreeObjects } from './ThreeScene';
import { ObjectFactory as OF } from '../../utils/three/ObjectFactory';


type Props = ThreeProps;

class CrystalStructure extends ThreeScene {

  private _crystalStructure: number[][] | null = null;
  private _cnt: number = 0;

  constructor(props: Props) {
    super(props);

    this.animate = this.animate.bind(this);
    this.createObjects = this.createObjects.bind(this);

    request
      .get('http://127.0.0.1:5000/test_crystal_structure/Mn2Sb')
      .end((err, res) => {
        if (err) {
          console.log(err);
          return;
        }

        this._crystalStructure = res.body.crystal_structure;
        console.log(this._crystalStructure);

        this._objects = this.createObjects();
        console.log(this._objects[100].obj.position);
        this.onObjectsUpdated();

        this.forceUpdate();
      })
  }

  createObjects(): ThreeObjects {
    const objs: ThreeObjects = []

    if (this._crystalStructure === null) {
      return objs;
    }

    for (let i = -3; i <= 3; i++) {
      for (let j = -3; j <= 3; j++) {
        for (let k = -3; k <= 3; k++) {
          objs.push({
            tag: `atom_${i}_${j}_${k}`,
            obj: OF.createArrow(
              'atom',
              (this._crystalStructure[0][0]*i + this._crystalStructure[1][0]*j + this._crystalStructure[2][0]*k)/3,
              (this._crystalStructure[0][1]*i + this._crystalStructure[1][1]*j + this._crystalStructure[2][1]*k)/3,
              (this._crystalStructure[0][2]*i + this._crystalStructure[1][2]*j + this._crystalStructure[2][2]*k)/3,
            ),
            objType: 'sphere'
          });
        }
      }
    }

    return objs;
  }

  animate(): void {
    this._cnt += 1;
    this._camera.position.x = 20.0 * Math.cos(0.01 * this._cnt);
    this._camera.position.z = 20.0 * Math.sin(0.01 * this._cnt);
    this._camera.lookAt(new THREE.Vector3(0, 0, 0));
    super.animate();
  }

  render() {
    return (
      <div>
        {super.render()}
        {this._crystalStructure}
      </div>
    )
  }
}

export default CrystalStructure;
