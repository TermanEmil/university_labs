class ArrayBuffer
{
	constructor(array, itemSize, numItems)
	{
		this.array = array;
		this.itemSize = itemSize;
		this.numItems = numItems;
	}
}

function randomTriagMovementAnim(targetObj)
{
	var anim = new Animation();
	anim.Update = function()
	{
		this.transform.Rotate(
			[
				100 * Time.deltaTime,
				300 * Time.deltaTime,
				50 * Time.deltaTime
			]);
	}

	var animator = new Animator();
	targetObj.AddComponent(animator);
	animator.AddAnim("idle", anim);
	return animator;
}

function initGameObjects()
{
	var vertices = new ArrayBuffer(
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

	var triag = new GameObject();
	triag.AddComponent(new Mesh(vertices, color));
	triag.transform.scale = [2, 2, 2];
	randomTriagMovementAnim(triag);

	var triag2 = new GameObject();
	triag2.AddComponent(new Mesh(vertices, color));
	triag2.transform.Translate([1, 2, 0]);
	randomTriagMovementAnim(triag2);
}
