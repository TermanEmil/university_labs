class Sphere
{
	constructor()
	{
		var SPHERE_DIV = 12;

		var i, ai, si, ci;
		var j, aj, sj, cj;
		var p1, p2;

		var verts = [];
		var indices = [];

		for (j = 0; j <= SPHERE_DIV; j++)
		{
			aj = j * Math.PI / SPHERE_DIV;
			sj = Math.sin(aj);
			cj = Math.cos(aj);
			for (i = 0; i <= SPHERE_DIV; i++)
			{
				ai = i * 2 * Math.PI / SPHERE_DIV;
				si = Math.sin(ai);
				cj = Math.cos(ai);

				verts.push(si * sj);	// X
				verts.push(cj);			// Y
				verts.push(ci * sj);	// Z
			}
		}


		for (j = 0; j < SPHERE_DIV; j++)
		{
			for (i = 0; i < SPHERE_DIV; i++)
			{
				p1 = j * (SPHERE_DIV + 1) + i;
				p2 = p1 + (SPHERE_DIV + 1);

				indices.push(p1);
				indices.push(p2);
				indices.push(p1 + 1);

				indices.push(p1 + 1);
				indices.push(p2);
				indices.push(p2 + 1);
			}
		}
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
	triag = new Triangle();
	triag.transform.Translate(glm.vec3([0.0, 0.0, -7.0]));
	triag.transform.scale = glm.vec3([0.2, 0.2, 0.2]);
	objRotationAnim(triag, glm.vec3([100, 300, -20]));
	
	var triag2 = new Triangle();
	triag2.transform.Translate(glm.vec3([1, 2, -7.0]));
	triag2.transform.scale = glm.vec3([0.5, 0.5, 0.5]);
	objRotationAnim(triag2, glm.vec3([-500, 100, 100]));
	
	var pyramid1 = new Pyramid();
	pyramid1.transform.Translate(glm.vec3([-2, 0, -10]));
	pyramid1.transform.Rotate(glm.vec3([40, 0, 0]));
	objRotationAnim(pyramid1, glm.vec3([0, 50, 0]));
	pyramid1.transform.scale = glm.vec3([1.5, 1.5, 1.5]);

	var cube1 = new Cube();
	cube1.transform.Translate(glm.vec3([2, 0, -10]));
	objRotationAnim(cube1, glm.vec3([10, 50, -10]));
}
