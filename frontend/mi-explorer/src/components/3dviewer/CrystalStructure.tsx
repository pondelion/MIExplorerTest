import React from 'react';
import request from 'superagent';
import * as THREE from 'three';
import ThreeScene from './ThreeScene';
import { Props as ThreeProps, ThreeObjects } from './ThreeScene';
import { ObjectFactory as OF } from '../../utils/three/ObjectFactory';
import CoordinateAxisScene from './CoordinateAxisScene';


type Props = ThreeProps;

class CrystalStructure extends CoordinateAxisScene {

  private _latticeMatrix: number[][] | null = null;
  private _sites: {[elem: string]: number[][]} | null = null;

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

        this._latticeMatrix = res.body.matrix;
        this._sites = res.body.sites;
        console.log(this._latticeMatrix);

        this._objects = this.createObjects();
        this.onObjectsUpdated();

        this.forceUpdate();
      })
  }

  createObjects(): ThreeObjects {
    const objs: ThreeObjects = super.createObjects();

    if (this._latticeMatrix === null) {
      return objs;
    }

    const COLORS: number[] = [
      0xB71C1C, 0x880E4F, 0x4A148C, 0x311B92, 0x1A237E, 0x0D47A1,
      0x006064, 0x1B5E20, 0x827717, 0xFF6F00, 0xBF360C, 0xEEEEEE,
    ]

    let i = 0;
    for (let elem in this._sites) {
      const col = COLORS[i];
      i += 4;
      const sites : number[][] = this._sites[elem]
      for (let j = 0; j < sites.length; j++) {
        const site = sites[j];
        for (let i = -2; i <= 2; i++) {
          for (let j = -2; j <= 2; j++) {
            for (let k = -2; k <= 2; k++) {
              objs.push({
                tag: `atom_${i}_${j}_${k}`,
                obj: OF.createSphere(
                  (site[0] + this._latticeMatrix[0][0]*i + this._latticeMatrix[1][0]*j + this._latticeMatrix[2][0]*k)/2,
                  (site[1] + this._latticeMatrix[0][1]*i + this._latticeMatrix[1][1]*j + this._latticeMatrix[2][1]*k)/2,
                  (site[2] + this._latticeMatrix[0][2]*i + this._latticeMatrix[1][2]*j + this._latticeMatrix[2][2]*k)/2,
                  0.3,
                  0.7,
                  col
                ),
                objType: 'sphere'
              });
            }
          }
        }
      }
    }

    return objs;
  }

  animate(): void {
    this._camera.position.x = 20.0 * Math.cos(0.02 * this._cnt);
    this._camera.position.z = 20.0 * Math.sin(0.02 * this._cnt);
    this._camera.lookAt(new THREE.Vector3(0, 0, 0));
    super.animate();
  }

  render() {
    return (
      <div>
        {super.render()}
        {this._latticeMatrix}
      </div>
    )
  }
}

export default CrystalStructure;
