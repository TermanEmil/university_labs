class Transform
{
	constructor(
		coords = [0.0, 0.0, 0.0],
		rotation = [0.0, 0.0, 0.0],
		scale = [1.0, 1.0, 1.0])
	{
		this.coords = coords;
		this.rotation = rotation;
		this.scale = scale;

		this.parent = null;
		this.children = [];
	}

	Translate(coords)
	{
		for (var i = 0; i < this.coords.length; i++)
			this.coords[i] += coords[i];
	}

	Rotate(rotation)
	{
		for (var i = 0; i < this.rotation.length; i++)
			this.rotation[i] += rotation[i];
	}
}
