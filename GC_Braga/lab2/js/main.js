var gl;
var shaderProgram;

function tick()
{
	window.requestAnimationFrame(function()
	{
		tick();
	});
	GameController.instance.Update();
}

function webGLStart()
{
	init();
	initGameObjects();

	tick();
}
