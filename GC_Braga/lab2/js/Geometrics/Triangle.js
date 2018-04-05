class Triangle // : GameObject
{
	constructor()
	{
		Object.setPrototypeOf(this, new GameObject());

		var verts = new ArrayBuffer(
		[
			 0.0,  1.0,  0.0,
			-1.0, -1.0,  0.0,
			 1.0, -1.0,  0.0
		],
		3, 3);

		var color = new ArrayBuffer(
		[
			1.0, 0.0, 0.0, 1.0,
			0.0, 1.0, 0.0, 1.0,
			0.0, 0.0, 1.0, 1.0
		],
		4, 3);

		this.AddComponent(new Mesh(verts, color));
	}
}