class GameController
{
	constructor()
	{
		this.objs = [new Time()];

		this.mvMatrix = mat4.create();
		this.pMatrix = mat4.create();
		this.mvMatrixStack = [];
	}

	Update()
	{
		this.Redraw();
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
		mat4.perspective(
			45,
			gl.viewportWidth / gl.viewportHeight,
			0.1,
			100.0,
			this.pMatrix);

		mat4.identity(this.mvMatrix);
	}
}