class Cube extends GameObject
{
	constructor()
	{
		super();
		
		var verts = new ArrayBuffer(
		[
			// Front face
			-1.0, -1.0,  1.0,
			 1.0, -1.0,  1.0,
			 1.0,  1.0,  1.0,
			-1.0,  1.0,  1.0,

			// Back face
			-1.0, -1.0, -1.0,
			-1.0,  1.0, -1.0,
			 1.0,  1.0, -1.0,
			 1.0, -1.0, -1.0,

			// Top face
			-1.0,  1.0, -1.0,
			-1.0,  1.0,  1.0,
			 1.0,  1.0,  1.0,
			 1.0,  1.0, -1.0,

			// Bottom face
			-1.0, -1.0, -1.0,
			 1.0, -1.0, -1.0,
			 1.0, -1.0,  1.0,
			-1.0, -1.0,  1.0,

			// Right face
			1.0, -1.0, -1.0,
			1.0,  1.0, -1.0,
			1.0,  1.0,  1.0,
			1.0, -1.0,  1.0,

			// Left face
			-1.0, -1.0, -1.0,
			-1.0, -1.0,  1.0,
			-1.0,  1.0,  1.0,
			-1.0,  1.0, -1.0,
		], 3, 24);

		var elementIndices = new ArrayBuffer(
			[
				0,  1,  2,    0,  2,  3,		// Front face
				4,  5,  6,    4,  6,  7,		// Back face
				8,  9,  10,   8,  10, 11,		// Top face
				12, 13, 14,   12, 14, 15,		// Bottom face
				16, 17, 18,   16, 18, 19,   // Right face
				20, 21, 22,   20, 22, 23		// Left face
  		], 1, 36);

		var colors =
		[
			[1.0, 0.0, 0.0, 1.0],     // Front face
			[1.0, 1.0, 0.0, 1.0],     // Back face
			[0.0, 1.0, 0.0, 1.0],     // Top face
			[1.0, 0.5, 0.5, 1.0],     // Bottom face
			[1.0, 0.0, 1.0, 1.0],     // Right face
			[0.0, 0.0, 1.0, 1.0],     // Left face
		];

		var unpackedColors = [];
		for (var i in colors)
			for (var j = 0; j < 4; j++)
				unpackedColors = unpackedColors.concat(colors[i]);

		var color = new ArrayBuffer(unpackedColors, 4, 24);
		var mesh = new Mesh(verts, color, elementIndices);

		this.AddComponent(mesh);
	}
}
