var gl;
var shaderProgram;
var gameController;

function degToRad(angle)
{
	return angle * (Math.PI / 180);
}

function tick()
{
	window.requestAnimationFrame(function()
	{
		tick();
	});
	gameController.Update();
}

function webGLStart()
{
	gameController = new GameController();

	var canvas = document.getElementById("my_canvas");
	gl = initGL(canvas);
	shaderProgram = initShaders(gl);

	var vertices =
	[
         0.0,  1.0,  0.0,
        -1.0, -1.0,  0.0,
         1.0, -1.0,  0.0
	];

	var colors = 
	[
		0.0, 1.0, 1.0, 1.0,
		1.0, 0.0, 0.0, 1.0,
		0.0, 0.0, 1.0, 1.0
	];

	gl.clearColor(0.0, 0.0, 0.0, 1.0);
	gl.enable(gl.DEPTH_TEST);

	var triag = new GameObject();
	triag.AddComponent(new Mesh(vertices, 3, 3));
	triag.transform.scale = [2, 2, 2];

	var triag2 = new GameObject();
	triag2.AddComponent(new Mesh(vertices, 3, 3));
	triag2.transform.Translate([1, 2, 0]);

	tick();
}