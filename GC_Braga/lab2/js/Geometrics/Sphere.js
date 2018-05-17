// SpicySnail - Miculet ViteOOk

class Sphere extends GameObject
{
	constructor(radius, edgeCount = 36)
	{
		super();

		var expectedSize = edgeCount * (edgeCount - 2) * 6 + edgeCount * 6;
		var retVal = [];
		var verts = [];

		var up = glm.vec3(0.0, radius, 0.0);
		var down = glm.vec3(0.0, -radius, 0.0);

		for (var i = 1; i < edgeCount; i++)
		{
			var percent = i * 1.0 / edgeCount;
			var currentHeight = -radius + (2 * percent * radius);
			var ring = this.CircleVertsUnconnected(
				Math.sqrt(radius * radius - currentHeight * currentHeight),
				edgeCount,
				currentHeight
			);
			verts = verts.concat(ring);
		}

		for (var i = 0; i < edgeCount - 2; i++)
		{
			for (var j = edgeCount * i; j < i * edgeCount + edgeCount - 1; j++)
			{
				retVal.push(
					verts[j],
					verts[j + edgeCount],
					verts[j + 1],
					verts[j + 1],
					verts[j + edgeCount],
					verts[j + edgeCount + 1]
				);
			}

			retVal.push(
				retVal.last(),
				verts[i * edgeCount],
				retVal[retVal.length - 3],

				retVal.last(),
				verts[i * edgeCount + edgeCount],
				verts[i * edgeCount]
			);
		}

		for (var i = 0; i < edgeCount - 1; i++)
		{
			retVal.push(
				verts[i],
				verts[i + 1],
				down,
				verts[verts.length - i - 1],
				verts[verts.length - i - 2],
				up
			);
		}

		retVal.push(
			verts[0],
			down,
			verts[edgeCount - 1],
			verts.last(),
			up,
			verts[verts.length - edgeCount]
		);

		if (retVal.length != expectedSize)
			console.error("retVal.length != expectedSize!!!!!");

		verts = [];
		for (var i = 0; i < retVal.length; i++)
		{
			var wow = retVal[i];
			verts.push(wow.x, wow.y, wow.z);
		}
		
		this.verts = new ArrayBuffer(verts, 3, retVal.length);

		var colors = [];
		for (var i = 0; i < retVal.length / 3; i++)
		{
			colors.push(
				1.0, 0.5, 1.0, 1.0,
				0.5, 1.0, 0.5, 1.0,
				0.5, 0.5, 1.0, 1.0,
			);
		}
		this.colors = new ArrayBuffer(colors, 4, retVal.length);
		this.AddComponent(new Mesh(this.verts, this.colors));
	}

	CircleVertsUnconnected(radius, edgeCount, yPos)
	{
		var retVal = [];

		for (var i = 0; i < edgeCount; i++)
		{
			var angle = i * 1.0 / edgeCount * 2 * Math.PI;
			retVal.push(glm.vec3(
				radius * Math.cos(angle),
				yPos,
				radius * Math.sin(angle)
			));
		}

		return retVal;
	}
}