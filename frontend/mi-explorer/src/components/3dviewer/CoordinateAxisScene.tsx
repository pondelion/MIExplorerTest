import React from 'react';
import * as THREE from 'three';
import ThreeScene from './ThreeScene';
import { ThreeObject, ThreeObjects } from './ThreeScene';
import { Props as ThreeProps } from './ThreeScene';
import { ObjectFactory as OF } from '../../utils/three/ObjectFactory';


type Props = ThreeProps;

class CoordinateAxisScene extends ThreeScene {

  constructor(props: Props) {
    super(props);

    this.animate = this.animate.bind(this);
    this.createObjects = this.createObjects.bind(this);

    this._objects = this.createObjects();
    this.onObjectsUpdated();

    this.forceUpdate();
  }

  animate(): void {
    this._camera.position.x = 3.0 * Math.cos(0.01 * this._cnt);
    this._camera.position.z = 3.0 * Math.sin(0.01 * this._cnt);
    this._camera.lookAt(new THREE.Vector3(0, 0, 0));
    super.animate();
  }

  createObjects(): ThreeObjects {
    const objs: ThreeObjects = [];

    objs.push({
      tag: 'x_axis',
      obj: OF.createArrow(
        'x_axis',
        0, 0, 0,
        1.0, 0.0, 0.0,
        0.5*Math.PI, 0.0, 0,
        3.0,
        0xFF0000,
        0.6, 0.6,
      ),
      objType: 'arrow'
    })

    objs.push({
      tag: 'y_axis',
      obj: OF.createArrow(
        'y_axis',
        0, 0, 0,
        0.0, 1.0, 0.0,
        0, 0.5*Math.PI, 0,
        3.0,
        0x00FF00,
        0.6, 0.6,
      ),
      objType: 'arrow'
    })

    objs.push({
      tag: 'z_axis',
      obj: OF.createArrow(
        'z_axis',
        0, 0, 0,
        0.0, 0.0, 1.0,
        0, 0, 0.5*Math.PI,
        3.0,
        0x0000FF,
        0.6, 0.6,
      ),
      objType: 'arrow'
    }) 
    return objs;
  }
}

export default CoordinateAxisScene;
