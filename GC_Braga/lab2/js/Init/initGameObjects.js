if (!Array.prototype.last)
{
	Array.prototype.last = function()
	{
        return this[this.length - 1];
    };
};

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

function objScaleAnim(targetObj, gradient, minScale)
{
	var anim = new Animation();
	anim.Update = function()
	{
		var scale = this.transform.scale;
		scale = scale['*'](Math.sin(Time.TotalTime()) * gradient)['+'](minScale);
		this.transform.scale = scale;
	}

	var animator = new Animator();
	targetObj.AddComponent(animator);
	animator.AddAnim("idle", anim);
	return animator;
}

function initGameObjects()
{
	var sphere1 = new Sphere(2, 50);
	sphere1.transform.Translate(glm.vec3([2.0, 0.0, -38.0]));
	sphere1.transform.scale = glm.vec3([0.3, 2.3, 0.3]);
	objRotationAnim(sphere1, glm.vec3([0, -200, -20]));
	objScaleAnim(sphere1, -0.4, glm.vec3([0.3, 2.3, 0.3])['*'](1.2));

	var sphere2 = new Sphere(2, 50);
	sphere2.transform.Translate(glm.vec3([-2.0, 2.0, -8.0]));
	sphere2.transform.scale = glm.vec3([0.3, 0.3, 0.3]);
	objRotationAnim(sphere2, glm.vec3([100, 300, -20]));
	objScaleAnim(sphere2, 0.2, glm.vec3([0.3, 0.3, 0.3])['*'](1.2));

	triag = new Triangle();
	triag.transform.Translate(glm.vec3([0.0, 0.0, -27.0]));
	triag.transform.scale = glm.vec3([0.2, 0.2, 0.2]);
	objRotationAnim(triag, glm.vec3([100, 300, -20]));
	objScaleAnim(triag, 1, glm.vec3([1.0, 1.0, 1.0])['*'](0.2));
	
	var triag2 = new Triangle();
	triag2.transform.Translate(glm.vec3([1, 2, -7.0]));
	triag2.transform.scale = glm.vec3([0.5, 0.5, 0.5]);
	objRotationAnim(triag2, glm.vec3([-500, 100, 100]));
	objScaleAnim(triag2, 0.6, glm.vec3([1.0, 1.0, 1.0])['*'](0.2));
	
	var pyramid1 = new Pyramid();
	pyramid1.transform.Translate(glm.vec3([-2, 0, -10]));
	pyramid1.transform.Rotate(glm.vec3([40, 0, 0]));
	objRotationAnim(pyramid1, glm.vec3([0, 50, 0]));
	pyramid1.transform.scale = glm.vec3([1.5, 1.5, 1.5]);
	objScaleAnim(pyramid1, -0.2, glm.vec3([1.0, 1.0, 1.0])['*'](1.2));

	var cube1 = new Cube();
	cube1.transform.Translate(glm.vec3([4, 0, -15]));
	objRotationAnim(cube1, glm.vec3([10, 50, -10]));
	objScaleAnim(cube1, 0.2, glm.vec3([1.0, 1.0, 1.0])['*'](1.2));
}
