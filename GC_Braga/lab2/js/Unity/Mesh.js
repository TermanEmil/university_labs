class Mesh
{
	constructor(verts, color, elementIndices)
	{
		this.modelMatrix = mat4.create();

		if (verts != null && verts != undefined)
		{
			this.verts = verts;
			this.verts.buf = gl.createBuffer();

			gl.bindBuffer(gl.ARRAY_BUFFER, this.verts.buf);
			gl.bufferData(
				gl.ARRAY_BUFFER,
				new Float32Array(this.verts.array),
				this.verts.drawType);
		}

		if (color != null && color != undefined)
		{
			this.color = color;
			this.color.buf = gl.createBuffer();
			gl.bindBuffer(gl.ARRAY_BUFFER, this.color.buf);
			gl.bufferData(
				gl.ARRAY_BUFFER,
				new Float32Array(this.color.array),
				this.color.drawType);
		}

		if (elementIndices != null && elementIndices != undefined)
		{
			this.elementIndices = elementIndices;
			this.elementIndices.buf = gl.createBuffer();
			gl.bindBuffer(gl.ELEMENT_ARRAY_BUFFER, this.elementIndices.buf);
			gl.bufferData(
				gl.ELEMENT_ARRAY_BUFFER,
				new Uint16Array(this.elementIndices.array),
				this.elementIndices.drawType);
		}
	}

	Update()
	{
		this.Render();
	}

	Render()
	{
		mat4.identity(this.modelMatrix);
		mat4.translate(this.modelMatrix, this.transform.pos.elements);
		mat4.scale(this.modelMatrix, this.transform.scale.elements);
		this.ApplyRotation();

		if (this.verts != null && this.verts != undefined)
		{
			gl.bindBuffer(gl.ARRAY_BUFFER, this.verts.buf);
			gl.vertexAttribPointer(
				shaderProgram.vertexPositionAttribute,
				this.verts.itemSize,
				gl.FLOAT,
				false,
				0,
				0);
		}

		if (this.color != null && this.color != undefined)
		{
			gl.bindBuffer(gl.ARRAY_BUFFER, this.color.buf);
			gl.vertexAttribPointer(
				shaderProgram.vertexColorAttribute,
				this.color.itemSize,
				gl.FLOAT,
				false,
				0,
				0);
		}

		if (this.elementIndices != null && this.elementIndices != undefined)
			gl.bindBuffer(gl.ELEMENT_ARRAY_BUFFER, this.elementIndices.buf);

		this.SetMatrixUniforms();
		if (this.elementIndices != null && this.elementIndices != undefined)
			gl.drawElements(
				gl.TRIANGLES,
				this.elementIndices.numItems,
				gl.UNSIGNED_SHORT,
				0);
		else
			gl.drawArrays(gl.TRIANGLES, 0, this.verts.numItems);
	}

	SetMatrixUniforms()
	{
		gl.uniformMatrix4fv(
			shaderProgram.modelMatrixUniform,
			false,
			this.modelMatrix);
		gl.uniformMatrix4fv(
			shaderProgram.viewMatrixUniform,
			false,
			Camera.instance.viewMatrix);
		gl.uniformMatrix4fv(
			shaderProgram.projMatrixUniform,
			false,
			Camera.instance.projMatrix);
	}

	ApplyRotation()
	{
		var rotation = this.transform.rotation.elements;
		var rotationIndexes = [0, 0, 0];

		for (var i = 0; i < rotation.length; i++)
		{
			rotationIndexes[i] = 1;
			mat4.rotate(
				this.modelMatrix,
				degToRad(rotation[i]),
				rotationIndexes);
			rotationIndexes[i] = 0;
		}
	}
}
