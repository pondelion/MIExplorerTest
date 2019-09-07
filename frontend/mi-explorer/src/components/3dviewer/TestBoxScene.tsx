import React from 'react';
import * as THREE from 'three';
import ThreeScene from './ThreeScene';
import { ThreeObject, ThreeObjects } from './ThreeScene';
import { Props as ThreeProps } from './ThreeScene';


type Props = ThreeProps;

class TestBoxScene extends ThreeScene {

  constructor(props: Props) {
    super(props);

    this.animate = this.animate.bind(this);
    this.createObjects = this.createObjects.bind(this);

    this._objects = this.createObjects();
  }

  animate(): void {
    this._objects[0].obj.rotation.x += 0.01;
    this._objects[0].obj.rotation.y += 0.01;
    super.animate();
  }

  createObjects(): ThreeObjects {
    const geometory = new THREE.BoxGeometry(1, 1, 1)
    const material = new THREE.MeshBasicMaterial({ color: '#FF0000' })
    const box = new THREE.Mesh(geometory, material);
    box.position.x = 0;
    box.position.y = 0;
    box.position.z = 0;

    const objs: ThreeObjects = [];
    objs.push({
      tag: 'box1',
      obj: box,
      objType: 'box'
    }) 
    return objs;
  }
}

export default TestBoxScene;
