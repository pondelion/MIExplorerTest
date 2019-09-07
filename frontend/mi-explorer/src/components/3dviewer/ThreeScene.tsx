import React from 'react';
import * as THREE from 'three';
import Button from '@material-ui/core/Button';


type Vec3 = {
  x: number,
  y: number,
  z: number,
};

export type ThreeObject = {
  tag?: string,
  obj: THREE.Mesh | THREE.ArrowHelper | THREE.Sprite,
  objType: 'box' | 'sphere' | 'line' | 'sprite' | 'other',
}

export type ThreeObjects = ThreeObject[];

export type Props = {
  width: number,
  height: number,
  cameraPos: Vec3,
  onObjectsChanged?: (objs: ThreeObjects) => {},
};


class ThreeScene extends React.Component<Props> {

  protected _scene: THREE.Scene;
  protected _camera: THREE.PerspectiveCamera;
  protected _renderer: THREE.WebGLRenderer;
  protected _mount: HTMLDivElement | null = null;
  protected _frameId: number | null = null;
  protected _objects: ThreeObjects = [];

  state = {
    camera_pos_x: 0
  };

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

    this.onButtonClick = this.onButtonClick.bind(this);
    this.animate = this.animate.bind(this);
    this.createObjects = this.createObjects.bind(this);

  }

  componentDidMount(): void {
    this._objects.map(obj => this._scene.add(obj.obj));
    if (this._mount) {
      this._mount.appendChild(this._renderer.domElement);
    }
    this.start();
  }

  componentWillUnmount(): void {
    this.stop()
    if (this._mount) {
      this._mount.removeChild(this._renderer.domElement);
    }
  }

  start(): void {
    if (!this._frameId) {
      this._frameId = requestAnimationFrame(this.animate);
    }
  }

  stop(): void {
    if (this._frameId) {
      cancelAnimationFrame(this._frameId);
    }
  }

  animate(): void {
    this._renderer.render(this._scene, this._camera);
    this._frameId = window.requestAnimationFrame(this.animate);
  }

  createObjects(): ThreeObjects {
    return [];
  }

  onButtonClick(): void {
    this._camera.position.x += 1;
    this.setState({camera_pos_x: this.state.camera_pos_x + 1});
  }

  render() {
    return (
      <div>
        <div
          style={{ width: this.props.width, height: this.props.height }}
          ref={(mount) => { this._mount = mount }}
        />
        <Button variant="contained" color="primary" onClick={this.onButtonClick}>
          {this._camera.position.x}
        </Button>
      </div>
    )
  }
}

export default ThreeScene;
