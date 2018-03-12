function initGL(canvas)
{
	var gl = canvas.getContext('experimental-webgl');
	gl.viewportWidth = canvas.width;
	gl.viewportHeight = canvas.height;

	return gl;
}

function getShader(gl, id)
{
	var shader;

	var shaderScript = document.getElementById(id);
	var str = "";
	var k = shaderScript.firstChild;
	
	while (k)
	{
		if (k.nodeType == 3)
			str += k.textContent;
		k = k.nextSibling;
	}

	if (shaderScript.type == "x-shader/x-fragment")
		shader = gl.createShader(gl.FRAGMENT_SHADER);
	else if (shaderScript.type == "x-shader/x-vertex")
		shader = gl.createShader(gl.VERTEX_SHADER);
	else
		return null;

	gl.shaderSource(shader, str);
	gl.compileShader(shader);

	if (!gl.getShaderParameter(shader, gl.COMPILE_STATUS))
	{
		alert(gl.getShaderInfoLog(shader));
		return null;
	}

	return shader;
}

function initShaders(gl)
{
	var fragmentShader = getShader(gl, "shader-fs");
	var vertexShader = getShader(gl, "shader-vs");

	var shaderProgram = gl.createProgram();
	gl.attachShader(shaderProgram, vertexShader);
	gl.attachShader(shaderProgram, fragmentShader);
	gl.linkProgram(shaderProgram);

	if (!gl.getProgramParameter(shaderProgram, gl.LINK_STATUS))
	{
		alert("Could not initialise shaders");
	}

	gl.useProgram(shaderProgram);

	shaderProgram.vertexPositionAttribute = gl.getAttribLocation(
		shaderProgram,
		"aVertexPosition")
	gl.enableVertexAttribArray(shaderProgram.vertexPositionAttribute);

	shaderProgram.vertexColorAttribute = gl.getAttribLocation(
		shaderProgram,
		"aVertexColor");
	gl.enableVertexAttribArray(shaderProgram.vertexColorAttribute);

	shaderProgram.pMatrixUniform = gl.getUniformLocation(
		shaderProgram,
		"uPMatrix");
	shaderProgram.mvMatrixUniform = gl.getUniformLocation(
		shaderProgram,
		"uMVMatrix");

	return shaderProgram;
}

function newTriag(gl, verts, coords)
{
	var triag = gl.createBuffer();
	gl.bindBuffer(gl.ARRAY_BUFFER, triag);
	gl.bufferData(gl.ARRAY_BUFFER, new Float32Array(verts), gl.STATIC_DRAW);
	triag.itemSize = 3;
	triag.numItems = 3;
	triag.coords = coords;

	return triag;
}

function initBuffers(gl, verts, colors)
{
	var buffers = new Object();

	buffers.verts = [];
	buffers.verts.push(newTriag(gl, verts, [0, 0.0, -10.0]));
	buffers.verts.push(newTriag(gl, verts, [2, 0.0, -15.0]));
	buffers.verts.push(newTriag(gl, verts, [2, 1.0, -15.0]));

	var colorBuf = gl.createBuffer();
	gl.bindBuffer(gl.ARRAY_BUFFER, colorBuf);
	gl.bufferData(gl.ARRAY_BUFFER, new Float32Array(colors), gl.STATIC_DRAW);
	colorBuf.itemSize = 4;
	colorBuf.numItems = 3;
	buffers.color = colorBuf;

	return buffers;
}

function setMatrixUniforms(gl, shaderProgram, mvMatrix, pMatrix)
{
	gl.uniformMatrix4fv(shaderProgram.pMatrixUniform, false, pMatrix);
	gl.uniformMatrix4fv(shaderProgram.mvMatrixUniform, false, mvMatrix);
}

function drawScene(gl, shaderProgram, buffers, mvMatrix, pMatrix)
{
	gl.viewport(0, 0, gl.viewportWidth, gl.viewportHeight);
	gl.clear(gl.COLOR_BUFFER_BIT | gl.DEPTH_BUFFER_BIT);
	mat4.perspective(
		45,
		gl.viewportWidth / gl.viewportHeight,
		0.1,
		100.0,
		pMatrix);

	mat4.identity(mvMatrix);
	for (var i = 0; i < buffers.verts.length; i++)
	{
		var element = buffers.verts[i];
		mat4.translate(mvMatrix, element.coords);

		gl.bindBuffer(gl.ARRAY_BUFFER, element);
		gl.vertexAttribPointer(
			shaderProgram.vertexPositionAttribute,
			element.itemSize,
			gl.FLOAT,
			false,
			0,
			0);

		gl.bindBuffer(gl.ARRAY_BUFFER, buffers.color);
		gl.vertexAttribPointer(
			shaderProgram.vertexColorAttribute,
			buffers.color.itemSize,
			gl.FLOAT,
			false,
			0,
			0);

		setMatrixUniforms(gl, shaderProgram, mvMatrix, pMatrix);
		gl.drawArrays(gl.TRIANGLES, 0, element.numItems);
	}
}

function webGLStart()
{
	var canvas = document.getElementById("my_canvas");
	var gl = initGL(canvas);
	var shaderProgram = initShaders(gl);

	var mvMatrix = mat4.create();
	var pMatrix = mat4.create();

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

	var buffers = initBuffers(gl, vertices, colors);
	gl.clearColor(0.0, 0.0, 0.0, 1.0);
	gl.enable(gl.DEPTH_TEST);

	drawScene(gl, shaderProgram, buffers, mvMatrix, pMatrix);
}