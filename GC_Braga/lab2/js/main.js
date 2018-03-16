var gl;
var shaderProgram;
var gameController;

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
	init();
	initGameObjects();

	tick();
}