var cam;

class GameController
{
	constructor()
	{
		GameController.instance = this;
	}

	Init()
	{
		this.objs = [new Time()];
		this.mvMatrixStack = [];

		this.input = new Input();
		this.camera = new Camera();
		cam = this.camera;
		cam.a = 0;
		// this.camera.transform.coords[Z] = 100;
	}

	Update()
	{
		this.Redraw();
		Camera.instance.ComputeViewMatrix();
		Camera.instance.ComputeProjMatrix();
		this.objs.forEach(function(obj)
		{
			obj.Update();
		});
	}

	PushMvMatrix()
	{
		var copy = mat4.create();
		mat4.set(this.mvMatrix, copy);
		this.mvMatrixStack.push(copy);
	}

	PopMvMatrix()
	{
		if (this.mvMatrixStack.length == 0)
			throw "Invalid popMatrix!";
		this.mvMatrix = this.mvMatrixStack.pop();
	}

	Redraw()
	{
		gl.viewport(0, 0, gl.viewportWidth, gl.viewportHeight);
		gl.clear(gl.COLOR_BUFFER_BIT | gl.DEPTH_BUFFER_BIT);

		// mat4.identity(Camera.instance.projMatrix);
		mat4.perspective(
			45.0,
			gl.viewportWidth / gl.viewportHeight,
			0.1,
			100.0,
			Camera.instance.projMatrix);
		// mat4.identity(Camera.instance.projMatrix);
		// console.log(Camera.instance.projMatrix);
		
		// console.log(GameController.instance.mvMatrix);
		// console.log(GameController.instance.pMatrix);
	}
}
