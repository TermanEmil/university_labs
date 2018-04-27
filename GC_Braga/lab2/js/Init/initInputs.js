function initInputs()
{
  Input.instance.onKeyDown['w'] = onAxisKeyDown;
  Input.instance.onKeyDown['a'] = onAxisKeyDown;
  Input.instance.onKeyDown['s'] = onAxisKeyDown;
  Input.instance.onKeyDown['d'] = onAxisKeyDown;

  Input.instance.onKeyDown['W'] = onAxisKeyDown;
  Input.instance.onKeyDown['A'] = onAxisKeyDown;
  Input.instance.onKeyDown['S'] = onAxisKeyDown;
  Input.instance.onKeyDown['D'] = onAxisKeyDown;
}

function onAxisKeyDown(event)
{
  var keyCode = String.fromCharCode(event.keyCode).toUpperCase();
  switch (keyCode[0])
  {
    case 'W':
      //GameController.instance.camera.transform.rotation[1] += GameController.instance.camera.xRotSpeed;
      //console.log(GameController.instance.camera.transform.rotation);
      triag.transform.coords[Z] += 0.1;
      console.log(triag.transform.coords);
      break;
    case 'A':
      break;
    case 'S':
      triag.transform.coords[Z] -= 0.1;
      console.log(triag.transform.coords);
      // GameController.instance.camera.transform.rotation[1] -= GameController.instance.camera.xRotSpeed;
      break;
    case 'D':
        break;
  }
}
