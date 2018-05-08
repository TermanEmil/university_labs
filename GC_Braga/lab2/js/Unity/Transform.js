class Transform
{
	constructor(
		coords = glm.vec3([0.0, 0.0, 0.0]),
		rotation = glm.vec3([0.0, 0.0, 0.0]),
		scale = glm.vec3([1.0, 1.0, 1.0]))
	{
		this.pos = coords;
		this.rotation = rotation;
		this.scale = scale;

		this.parent = null;
		this.children = [];
	}

	Translate(coords)
	{
		for (var i = 0; i < coords.elements.length; i++)
			this.pos.elements[i] += coords.elements[i];
	}

	Rotate(rotation)
	{
		for (var i = 0; i < rotation.elements.length; i++)
			this.rotation.elements[i] += rotation.elements[i];
	}
}
