class Camera extends GameObject
{
  constructor()
  {
    super();

    Camera.instance = this;

    this.viewMatrix = mat4.create();
    this.projMatrix = mat4.create();
    mat4.identity(this.viewMatrix);

    this.xRotSpeed = 0.5;
    this.yRotSpeed = 0.5;

    this.fieldOfViewInRadians = Math.PI * 0.5;
    this.aspectRatio = gl.viewportWidth / gl.viewportHeight;
    this.nearClippingPlaneDistance = 1;
    this.farClippingPlaneDistance = 50;
  }

  Mat4ApplyPresence(mvMatrix)
  {
    mat4.rotate(mvMatrix, degToRad(-this.transform.rotation[X]), [1, 0, 0]);
    mat4.rotate(mvMatrix, degToRad(-this.transform.rotation[Y]), [0, 1, 0]);
    mat4.translate(mvMatrix,
      [
        -this.transform.coords[X],
        -this.transform.coords[Y],
        -this.transform.coords[Z]
      ]);
  }

  GetPerspectiveMatrix()
  {
    var f = 1.0 / Math.tan(this.fieldOfViewInRadians / 2);
    var rangeInv = 1 / (near - far);

    var near = this.nearClippingPlaneDistance;
    var far = this.farClippingPlaneDistance;
    var aspectRatio = this.aspectRatio;

    return
    [
      f / aspectRatio, 0,                          0,   0,
      0,               f,                          0,   0,
      0,               0,    (near + far) * rangeInv,  -1,
      0,               0,  near * far * rangeInv * 2,   0
    ];
  }
}
