class Mesh
{
	constructor(verts, color)
	{
		if (verts != null && verts != undefined)
		{
			this.verts = verts;
			this.verts.buf = gl.createBuffer();
			gl.bindBuffer(gl.ARRAY_BUFFER, this.verts.buf);
			gl.bufferData(
				gl.ARRAY_BUFFER,
				new Float32Array(this.verts.array), gl.STATIC_DRAW);
		}

		if (color != null && color != undefined)
		{
			this.color = color;
			this.color.buf = gl.createBuffer();
			gl.bindBuffer(gl.ARRAY_BUFFER, this.color.buf);
			gl.bufferData(
				gl.ARRAY_BUFFER,
				new Float32Array(this.color.array), gl.STATIC_DRAW);
		}
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

		gl.bindBuffer(gl.ARRAY_BUFFER, this.verts.buf);
		gl.vertexAttribPointer(
			shaderProgram.vertexPositionAttribute,
			this.verts.itemSize,
			gl.FLOAT,
			false,
			0,
			0);

		gl.bindBuffer(gl.ARRAY_BUFFER, this.color.buf);
		gl.vertexAttribPointer(
			shaderProgram.vertexColorAttribute,
			this.color.itemSize,
			gl.FLOAT,
			false,
			0,
			0);

		// Mesh.SetMatrixUniforms();
		// gl.bindBuffer(gl.ELEMENT_ARRAY_BUFFER, this.verts.buf);
		// Mesh.SetMatrixUniforms();
		// gl.drawElements(gl.TRIANGLES, this.verts.numItems, gl.UNSIGNED_SHORT, 0);

		Mesh.SetMatrixUniforms();
		gl.drawArrays(gl.TRIANGLES, 0, this.verts.numItems);

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
