if (!Array.prototype.last)
{
	Array.prototype.last = function()
	{
        return this[this.length - 1];
    };
};

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
			var currentHeight = -radius * (2 * percent * radius);
			var ring = this.CircleVertsUnconnected(
				Math.sqrt(radius * radius - currentHeight * currentHeight),
				edgeCount,
				currentHeight
			);
			verts = verts.concat(ring);
			// verts.push(ring);// verts.last(), ring[0], ring.last());
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
			verts = verts.concat(retVal[i].elements);
		
		this.verts = new ArrayBuffer(verts, 3, retVal.length / 3);

		var colors = [];
		for (var i = 0; i < retVal.length / 9; i++)
		{
			colors.push(
				1.0, 0.0, 0.0, 1.0,
				0.0, 1.0, 0.0, 1.0,
				0.0, 0.0, 1.0, 1.0,
			);
		}
		this.colors = new ArrayBuffer(colors, 4, retVal.length / 3);
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

function objRotationAnim(targetObj, rotation)
{
	var anim = new Animation();
	anim.Update = function()
	{
		this.transform.Rotate(rotation['*'](Time.deltaTime));
	}

	var animator = new Animator();
	targetObj.AddComponent(animator);
	animator.AddAnim("idle", anim);
	return animator;
}

var triag;

function initGameObjects()
{
	var sphere = new Sphere(5);
	sphere.transform.Translate(glm.vec3([0.0, 0.0, -7.0]));

	// triag = new Triangle();
	// triag.transform.Translate(glm.vec3([0.0, 0.0, -7.0]));
	// triag.transform.scale = glm.vec3([0.2, 0.2, 0.2]);
	// objRotationAnim(triag, glm.vec3([100, 300, -20]));
	
	// var triag2 = new Triangle();
	// triag2.transform.Translate(glm.vec3([1, 2, -7.0]));
	// triag2.transform.scale = glm.vec3([0.5, 0.5, 0.5]);
	// objRotationAnim(triag2, glm.vec3([-500, 100, 100]));
	
	// var pyramid1 = new Pyramid();
	// pyramid1.transform.Translate(glm.vec3([-2, 0, -10]));
	// pyramid1.transform.Rotate(glm.vec3([40, 0, 0]));
	// objRotationAnim(pyramid1, glm.vec3([0, 50, 0]));
	// pyramid1.transform.scale = glm.vec3([1.5, 1.5, 1.5]);

	// var cube1 = new Cube();
	// cube1.transform.Translate(glm.vec3([2, 0, -10]));
	// objRotationAnim(cube1, glm.vec3([10, 50, -10]));
}
