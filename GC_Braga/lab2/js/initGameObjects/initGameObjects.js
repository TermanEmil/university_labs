class Cube
{
	constructor()
	{
		Object.setPrototypeOf(this, new GameObject());

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
		{
			for (var j=0; j < 4; j++)
				unpackedColors = unpackedColors.concat(colors[i]);
		}
		console.log();
		var color = new ArrayBuffer(unpackedColors, 4, 24);

		var mesh = new Mesh(verts, color);
		this.AddComponent(mesh);
	}
}

function objRotationAnim(targetObj, rotation)
{
	var anim = new Animation();
	anim.Update = function()
	{
		this.transform.Rotate(rotation.map(x => x * Time.deltaTime));
	}

	var animator = new Animator();
	targetObj.AddComponent(animator);
	animator.AddAnim("idle", anim);
	return animator;
}

function initGameObjects()
{
	var triag = new Triangle();
	triag.transform.Translate([-3, -1, 0]);
	triag.transform.scale = [0.2, 0.2, 0.2];
	objRotationAnim(triag, [100, 300, -20]);

	var triag2 = new Triangle();
	triag2.transform.Translate([1, 2, 0]);
	triag2.transform.scale = [0.2, 0.2, 0.2];
	objRotationAnim(triag2, [-500, 100, 100]);

	var pyramid1 = new Pyramid();
	pyramid1.transform.Translate([-7, 5, -10]);
	pyramid1.transform.Rotate([40, 0, 0]);
	objRotationAnim(pyramid1, [0, 50, 0]);
	pyramid1.transform.scale = [1.5, 1.5, 1.5];

	var cube1 = new Cube();
	objRotationAnim(cube1, [10, 50, 10]);
}
