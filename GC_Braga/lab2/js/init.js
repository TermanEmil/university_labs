function init()
{
	gameController = new GameController();

	gl = initGL(document.getElementById("my_canvas"));
	shaderProgram = initShaders(gl);
	gl.clearColor(0.0, 0.0, 0.0, 1.0);
	gl.enable(gl.DEPTH_TEST);

	// Object.setPrototypeOf(Pyramid.prototype, new GameObject());
}