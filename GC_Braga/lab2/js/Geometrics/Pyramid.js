class Pyramid extends GameObject
{
	constructor()
	{
		super();

		var verts = new ArrayBuffer(
		[
			// Front face
			 0.0,  1.0,  0.0,
			-1.0, -1.0,  1.0,
			 1.0, -1.0,  1.0,
			// Right face
			 0.0,  1.0,  0.0,
			 1.0, -1.0,  1.0,
			 1.0, -1.0, -1.0,
			// Back face
			 0.0,  1.0,  0.0,
			 1.0, -1.0, -1.0,
			-1.0, -1.0, -1.0,
			// Left face
			 0.0,  1.0,  0.0,
			-1.0, -1.0, -1.0,
			-1.0, -1.0,  1.0
		], 3, 12);

		var color = new ArrayBuffer(
		[
			// Front face
			1.0, 0.0, 0.0, 1.0,
			0.0, 1.0, 0.0, 1.0,
			0.0, 0.0, 1.0, 1.0,
			// Right face
			1.0, 0.0, 0.0, 1.0,
			0.0, 0.0, 1.0, 1.0,
			0.0, 1.0, 0.0, 1.0,
			// Back face
			1.0, 0.0, 0.0, 1.0,
			0.0, 1.0, 0.0, 1.0,
			0.0, 0.0, 1.0, 1.0,
			// Left face
			1.0, 0.0, 0.0, 1.0,
			0.0, 0.0, 1.0, 1.0,
			0.0, 1.0, 0.0, 1.0
		], 4, 12);

		this.AddComponent(new Mesh(verts, color));
	}
}
