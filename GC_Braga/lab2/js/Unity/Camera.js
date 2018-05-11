class Camera extends GameObject
{
  constructor()
  {
    super();

    Camera.instance = this;

    this.viewMatrix = mat4.create();
    this.projMatrix = mat4.create();
    mat4.identity(this.viewMatrix);

    this.transform.rotation[X] = -90;

    this.xRotSpeed = 0.5;
    this.yRotSpeed = 0.5;
    this.moveSpeed = glm.vec3(0.1, 0.1, 0.1);

    this.fieldOfViewInRadians = Math.PI * 0.5;
    this.aspectRatio = gl.viewportWidth / gl.viewportHeight;
    this.nearClippingPlaneDistance = 1;
    this.farClippingPlaneDistance = 50;

    this.rb = new RigidBody();
    this.AddComponent(this.rb);
  }

  ComputeViewMatrix()
  {
    var eye = this.transform.pos;
    var up = glm.vec3(0, 1, 0);
    var front = this.Front();

    this.viewMatrix = glm.lookAt(eye, eye['+'](front), up).elements;
  }

  ApplyRotation(rotation, matrix)
	{
		var rotationIndexes = [0, 0, 0];

		for (var i = 0; i < rotation.length; i++)
		{
			rotationIndexes[i] = 1;
			mat4.rotate(
				matrix,
				degToRad(rotation[i]),
				rotationIndexes);
			rotationIndexes[i] = 0;
		}
	}

  ComputeProjMatrix()
  {
    mat4.perspective(
			45.0,
			gl.viewportWidth / gl.viewportHeight,
			0.1,
			100.0,
			this.projMatrix);
  }

  Move(direction)
  {
    this.rb.velocity = this.rb.velocity['+'](this.moveSpeed['*'](this.Front()['*'](direction)));
  }

  Front()
  {
    var rotation = this.transform.rotation;

    return glm.vec3(
      Math.cos(glm.radians(rotation.x)) * Math.cos(glm.radians(rotation.y)),
      Math.sin(glm.radians(rotation.y)),
      Math.sin(glm.radians(rotation.x)) * Math.cos(glm.radians(rotation.y))
    );
  }
}
