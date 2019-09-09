import * as THREE from 'three';


export class ObjectFactory {

  static createSphere(
    pos_x: number = 0.0,
    pos_y: number = 0.0,
    pos_z: number = 0.0,
    radius: number = 1.0,
    opacity: number = 1.0,
    color: number = 0x22DD22,
  ): THREE.Mesh {
    const sphereRadius = radius;
    const sphereGeometry = new THREE.SphereGeometry(sphereRadius, 20, 20);
    const sphereMaterial = new THREE.MeshLambertMaterial({
      color: color,
      opacity: opacity,
      transparent: true,
      side: THREE.DoubleSide,
      depthWrite: false
    })
    const sphere = new THREE.Mesh(sphereGeometry, sphereMaterial);

    sphere.position.x = pos_x;
    sphere.position.y = pos_y;
    sphere.position.z = pos_z;
    sphere.castShadow = true;

    return sphere;
  }

  static createBox(
    pos_x: number = 0,
    pos_y: number = 0,
    pos_z: number = 0,
    size_x: number = 1.0,
    size_y: number = 1.0,
    size_z: number = 1.0,
    opacity: number = 1.0,
    color: number = 0xff0000,
  ): THREE.Mesh {
    const box = new THREE.Mesh(
        new THREE.BoxGeometry(size_x, size_y, size_z),
        new THREE.MeshLambertMaterial({
          color: color,
          opacity: opacity,
          transparent: true,
          side: THREE.DoubleSide,
          depthWrite: false
        })
    );
    box.receiveShadow = true;

    box.position.set(pos_x, pos_y, pos_z);
    return box;
  }

  static createPlane(
    pos_x: number = 0,
    pos_y: number = 0,
    pos_z: number = 0,
    rotation_x: number = -0.5*Math.PI, 
    rotation_y: number = 0,
    rotation_z: number = 0,
    color: number = 0xff0000,
    size_h: number = 50,
    size_w:number = 50,
  ): THREE.Mesh {
    const planeGeometry = new THREE.PlaneGeometry(size_w, size_h, 1, 1);
    const planeMaterial = new THREE.MeshLambertMaterial({color: color});
    const plane = new THREE.Mesh(planeGeometry, planeMaterial);
    plane.receiveShadow = true;

    plane.rotation.x = rotation_x;
    plane.rotation.y = rotation_y;
    plane.rotation.z = rotation_z;
    plane.position.x = pos_x;
    plane.position.y = pos_y;
    plane.position.z = pos_z;

    return plane;
  }

  static createArrow(
    name: string,
    pos_x: number = 0,
    pos_y: number = 0,
    pos_z: number = 0,
    dir_x: number = 0,
    dir_y: number = 1,
    dir_z: number = 0,
    rotation_x: number = -Math.PI,
    rotation_y: number = 0,
    rotation_z: number = 0,
    length: number = 0.8,
    color: number = 0x00ff00,
    headWidth: number = 0.3,
    headLength: number = 0.3
  ): THREE.ArrowHelper {
    const dir = new THREE.Vector3(dir_x, dir_y, dir_z);
    const pos = new THREE.Vector3(pos_x, pos_y, pos_z);
    const arrowHelper = new THREE.ArrowHelper(dir, pos, length, color, 
                                              headWidth=headWidth,
                                              headLength=headLength);
    arrowHelper.name = name;
    arrowHelper.rotation.x = rotation_x;
    arrowHelper.rotation.y = rotation_y;
    arrowHelper.rotation.z = rotation_z;

    return arrowHelper;
  }

  static createSprite(
    pos_x: number = 0,
    pos_y: number = 0,
    pos_z: number = 0,
    scale: number = 0.2,
    color: number = 0x0000ee,
  ): THREE.Sprite {
    const material = new THREE.SpriteMaterial({color: color});
    const sprite = new THREE.Sprite(material);
    sprite.position.x = pos_x;
    sprite.position.y = pos_y;
    sprite.position.z = pos_z;
    sprite.scale.x = scale;
    sprite.scale.y = scale;
    sprite.scale.z = scale;

    return sprite;
  }
}

export default ObjectFactory;
