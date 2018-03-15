class Mesh
{
	constructor(verts = [], itemSize = 3, numItems = 3)
	{
		this.verts = verts;
	
		this.vertsBuf = gl.createBuffer();
		gl.bindBuffer(gl.ARRAY_BUFFER, this.vertsBuf);
		gl.bufferData(gl.ARRAY_BUFFER, new Float32Array(verts), gl.STATIC_DRAW);
		this.itemSize = itemSize;
		this.numItems = numItems;
	}

	Update()
	{
		this.Render();
	}

	Render()
	{
		mat4.identity(gameController.mvMatrix);
		mat4.translate(
			gameController.mvMatrix,
			this.transform.coords);

		gameController.PushMvMatrix();
		mat4.scale(gameController.mvMatrix, this.transform.scale);
		this.ApplyRotation();

		gl.bindBuffer(gl.ARRAY_BUFFER, this.vertsBuf);
		gl.vertexAttribPointer(
			shaderProgram.vertexPositionAttribute,
			this.itemSize,
			gl.FLOAT,
			false,
			0,
			0);

		// gl.bindBuffer(gl.ARRAY_BUFFER, buffers.color);
		// gl.vertexAttribPointer(
		// 	shaderProgram.vertexColorAttribute,
		// 	buffers.color.itemSize,
		// 	gl.FLOAT,
		// 	false,
		// 	0,
		// 	0);

		Mesh.SetMatrixUniforms();
		gl.drawArrays(gl.TRIANGLES, 0, this.numItems);

		gameController.PopMvMatrix();
	}

	static SetMatrixUniforms()
	{
		gl.uniformMatrix4fv(
			shaderProgram.pMatrixUniform, false, gameController.pMatrix);
		gl.uniformMatrix4fv(
			shaderProgram.mvMatrixUniform, false, gameController.mvMatrix);
	}

	ApplyRotation()
	{
		var rotation = this.transform.rotation;
		var rotationIndexes = [0, 0, 0];

		for (var i = 0; i < rotation.length; i++)
		{
			rotationIndexes[i] = 1;
			mat4.rotate(
				gameController.mvMatrix,
				degToRad(rotation[i]),
				rotationIndexes);
			rotationIndexes[i] = 0;
		}
	}
}
