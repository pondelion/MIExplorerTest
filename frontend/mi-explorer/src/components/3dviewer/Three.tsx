import React from 'react';
import * as THREE from 'three';


type Vec3 = {
  x: number,
  y: number,
  z: number,
};

type Props = {
  width: number,
  height: number,
  cameraPos: Vec3,
};


export class ThreeScene extends React.Component<Props> {

  private _scene: THREE.Scene;
  private _camera: THREE.PerspectiveCamera;
  private _renderer: THREE.WebGLRenderer;
  private _box: THREE.Mesh;
  private _mount: HTMLDivElement | null = null;
  private _frameId: number | null = null;

  constructor(props: Props) {
    super(props);

    this._scene = new THREE.Scene();

    const width = this.props.width;
    const height = this.props.height;
    this._camera = new THREE.PerspectiveCamera(
      45,
      width / height,
      0.1,
      1000
    );

    this._camera.position.x = this.props.cameraPos.x;
    this._camera.position.y = this.props.cameraPos.y;
    this._camera.position.z = this.props.cameraPos.z;

    this._camera.lookAt(new THREE.Vector3(0, 0, 0));

    this._renderer = new THREE.WebGLRenderer({ antialias: true });
    this._renderer.setSize(width, height);

    const geometory = new THREE.BoxGeometry(1, 1, 1)
    const material = new THREE.MeshBasicMaterial({ color: '#FF0000' })
    this._box = new THREE.Mesh(geometory, material);
    this._box.position.x = 0;
    this._box.position.y = 0;
    this._box.position.z = 0;
    
    this._scene.add(this._box);
  }

  componentDidMount() {
    if (this._mount) {
      this._mount.appendChild(this._renderer.domElement);
    }
    this.start();
  }

  componentWillUnmount() {
    this.stop()
    if (this._mount) {
      this._mount.removeChild(this._renderer.domElement);
    }
  }

  start = () => {
    if (!this._frameId) {
      this._frameId = requestAnimationFrame(this.animate);
    }
  }

  stop = () => {
    if (this._frameId) {
      cancelAnimationFrame(this._frameId);
    }
  }

  animate = () => {
    this._box.rotation.x += 0.01
    this._box.rotation.y += 0.01
    this.renderScene()
    this._frameId = window.requestAnimationFrame(this.animate)
  }

  renderScene = () => {
    this._renderer.render(this._scene, this._camera)
  }

  render() {
    return (
      <div
        style={{ width: this.props.width, height: this.props.height }}
        ref={(mount) => { this._mount = mount }}
      />
    )
  }
}

export default ThreeScene;
