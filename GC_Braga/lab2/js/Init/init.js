var X = 0;
var Y = 1;
var Z = 2;

function init()
{
	g_gameController = new GameController();

	gl = initGL(document.getElementById("my_canvas"));
	shaderProgram = initShaders(gl);
	gl.clearColor(0.0, 0.0, 0.0, 1.0);
	gl.enable(gl.DEPTH_TEST);

	g_gameController.Init();
	initInputs();
	// Object.setPrototypeOf(Pyramid.prototype, new GameObject());
}
