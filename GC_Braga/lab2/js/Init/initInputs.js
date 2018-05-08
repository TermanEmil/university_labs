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

  Input.instance.onKeyDown['1'] = onAxisKeyDown;
  Input.instance.onKeyDown['2'] = onAxisKeyDown;
  Input.instance.onKeyDown['3'] = onAxisKeyDown;
  Input.instance.onKeyDown['4'] = onAxisKeyDown;
}

function onAxisKeyDown(event)
{
  var keyCode = String.fromCharCode(event.keyCode).toUpperCase();

  switch (keyCode[0])
  {
    case 'W':
      Camera.instance.Move(1);
      console.log(Camera.instance.transform.pos);
      break;
    case 'S':
      Camera.instance.Move(-1);
      break;
    case 'A':
      break;
    case 'D':
      break;
    case '1':
      Camera.instance.rb.angularVel[0] -= 0.2;
      break;
    case '2':
      Camera.instance.rb.angularVel[0] += 0.2;
      break;
    case '3':
    Camera.instance.rb.angularVel[1] -= 0.2;
      break;
    case '4':
    Camera.instance.rb.angularVel[1] += 0.2;
      break;
  }
}
